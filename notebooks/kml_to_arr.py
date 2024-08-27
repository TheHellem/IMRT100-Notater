import xml.etree.ElementTree as ET
from datetime import datetime

# Script for å lage arrayer fra .kml filer samlet inn i IMRT100

# Funksjon for å lage arr fra RTK-data
def extract_coordinates_kml_RTK (kml_file):
    tree = ET.parse(kml_file)
    root = tree.getroot()
    
    # Namespace er noe vi må ha med siden det ikke er en XML fil
    namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

    # Går igjennom alle punktene - må her også ha spesielt format pga kml-fil
    coordinates = []
    for placemark in root.findall('.//kml:Placemark', namespace):
            longitude = placemark.find('.//kml:SimpleData[@name="Longitude"]', namespace).text
            latitude = placemark.find('.//kml:SimpleData[@name="Latitude"]', namespace).text
            coordinates.append([float(longitude), float(latitude)])
    return coordinates


def extract_coordinates_kml_mobil (kml_file):
    tree = ET.parse(kml_file)
    root = tree.getroot()

    namespace = {'kml': 'http://www.opengis.net/kml/2.2'}
    coordinates_text = root.find('.//kml:coordinates', namespace).text.strip()

    coordinates = []
    for coordinate in coordinates_text.split():
        lon, lat, _ = map(float, coordinate.split(','))
        coordinates.append([lon, lat])
    return coordinates

def extract_coordinates_kml_arduino (kml_file):
    tree = ET.parse(kml_file)
    root = tree.getroot()

    ns = {'kml': 'http://www.opengis.net/kml/2.2'}

    # Definerer tidsintervallet vi er interessert i (når den lå på punktet)
    start_time = datetime.strptime('2024-08-27T09:50:30Z', '%Y-%m-%dT%H:%M:%SZ')
    end_time = datetime.strptime('2024-08-27T09:55:30Z', '%Y-%m-%dT%H:%M:%SZ')

    coordinates = []

    for placemark in root.findall('.//kml:Placemark', ns):
        timestamp_element = placemark.find('.//kml:TimeStamp/kml:when', ns)
        point = placemark.find('.//kml:Point/kml:coordinates', ns)
        
        if timestamp_element is not None and point is not None:
            try:
                timestamp = datetime.strptime(timestamp_element.text.strip(), '%Y-%m-%dT%H:%M:%S.%fZ')
            except ValueError:
                timestamp = datetime.strptime(timestamp_element.text.strip(), '%Y-%m-%dT%H:%M:%SZ')
            
            if start_time <= timestamp <= end_time:
                coords = point.text.strip()
                lon, lat, *alt = map(float, coords.split(','))
                #formatted_time = timestamp.strftime('%H:%M:%S') # For å finne sabotasjepunktet
                coordinates.append([lon, lat])

    return coordinates

