import matplotlib.pyplot as plt
import numpy as np

def plot_coordinates_with_error_bars(df):
    """
    Plots coordinates with error bars for each method in the DataFrame.
    
    Parameters:
    - df: DataFrame containing columns 'Metode', 'Gjennomsnitt [m]', and 'Standardavvik [m]'.
    """
    plt.figure(figsize=(10, 6))
    
    # Define colors and markers for each method
    colors = ['black', 'red', 'blue']
    markers = ['o', '^', 's']
    
    for i, row in df.iterrows():
        method = row['Metode']
        avg = row['Gjennomsnitt [m]']
        stddev = row['Standardavvik [m]']
        
        # Scatter plot with error bars
        plt.errorbar(
            avg[0], avg[1], 
            xerr=stddev[0], yerr=stddev[1], 
            fmt=markers[i], color=colors[i], 
            label=method, capsize=5
        )
    
    # Setting the title and labels
    plt.title('Gjennomsnittskoordinater for de ulike metodene')
    plt.xlabel('Ø [m]')
    plt.ylabel('N [m]')
    
    # Add grid and legend
    plt.grid(True)
    plt.legend()
    
    # Display the plot
    plt.show()

# Example usage:
# Create the DataFrame
# data = {
#     'Metode': ['RTK', 'Mobiltelefon', 'Arduino-enhet'],
#     'Antall punkter': [7, 273, 194],
#     'Gjennomsnitt [m]': [
#         [600011.179, 6615540.58],
#         [600011.88, 6615540.66],
#         [600011.0, 6615540.7]
#     ],
#     'Standardavvik [m]': [
#         [0.006, 0.015],
#         [0.16, 0.13],
#         [0.4, 0.6]
#     ]
# }
# df = pd.DataFrame(data)

# # Plot the data with error bars
# plot_coordinates_with_error_bars(df)
