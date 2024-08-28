
# Funksjoner for å finne index på ytterliggende punkt (sabotasjepunkt)

def find_furthest_east(coordinates):
    # Ensure there are coordinates in the array
    if not coordinates:
        return None, None

    # Initialize variables to store the maximum longitude, index, and the corresponding coordinate
    max_longitude = float('-inf')
    furthest_east_index = None
    furthest_east_coordinate = None

    for index, coord in enumerate(coordinates):
        longitude = coord[0]
        # Check if the current longitude is greater than the max found so far
        if longitude > max_longitude:
            max_longitude = longitude
            furthest_east_index = index
            furthest_east_coordinate = coord

    return furthest_east_index, furthest_east_coordinate


def find_furthest_west(coordinates):
    # Ensure there are coordinates in the array
    if not coordinates:
        return None, None

    # Initialize variables to store the minimum longitude, index, and the corresponding coordinate
    min_longitude = float('inf')
    furthest_west_index = None
    furthest_west_coordinate = None

    for index, coord in enumerate(coordinates):
        longitude = coord[0]
        # Check if the current longitude is less than the min found so far
        if longitude < min_longitude:
            min_longitude = longitude
            furthest_west_index = index
            furthest_west_coordinate = coord

    return furthest_west_index, furthest_west_coordinate

