import matplotlib.pyplot as plt


def plot_multiple_coordinates(*coordinate_sets, labels=None, colors=None, markers=None, space_value=1):
    """
    Plots multiple sets of coordinates on the same scatter plot.
    
    Parameters:
    - coordinate_sets: Variable number of coordinate sets, each as a list of tuples [(long, lat), (long, lat), ...].
    - labels: Optional list of labels for each set. Defaults to 'Set 1', 'Set 2', etc.
    - colors: Optional list of colors for each set. Defaults to a predefined list of colors.
    - markers: Optional list of markers for each set. Defaults to '.' for the first set, 'o' for the second, etc.
    - space_value: Optional float to adjust the spacing around the points in the plot.
    """
    
    # Setting default labels, colors, and markers if not provided
    if labels is None:
        labels = [f'Set {i+1}' for i in range(len(coordinate_sets))]
    
    if colors is None:
        colors = ['black', 'red', 'blue', 'green', 'purple', 'orange']
    
    if markers is None:
        markers = ['.', '.', '^', 's', 'D', 'v']
    
    plt.figure(figsize=(10, 6))
    
    # Initialize min and max values for all sets
    all_longs = []
    all_lats = []
    
    # Plot each set
    for i, coordinates in enumerate(coordinate_sets):
        long, lat = zip(*coordinates)
        all_longs.extend(long)
        all_lats.extend(lat)
        
        plt.scatter(long, lat, c=colors[i % len(colors)], marker=markers[i % len(markers)], label=labels[i])
    
    # Adjust axis limits based on all points
    plt.xlim(min(all_longs) - space_value, max(all_longs) + space_value)
    plt.ylim(min(all_lats) - space_value, max(all_lats) + space_value)
    
    # Adding title and labels
    plt.title('Spredningsdiagram av de ulike GNSS mottakerne')
    plt.xlabel('Ø [m]')
    plt.ylabel('N [m]')
    
    # Optional: Add grid
    plt.grid(True)
    
    # Display the plot with a legend
    plt.legend()
    plt.show()

# Example usage:
# mobile_coordinates = extract_coordinates_kml_mobil('dataset/trygve_data.kml')
# rtk_coordinates = extract_coordinates_kml_RTK('dataset/RTK.kml')

# plot_multiple_coordinates(mobile_coordinates, rtk_coordinates, labels=['Mobile GNSS', 'RTK'], colors=['black', 'red'])
