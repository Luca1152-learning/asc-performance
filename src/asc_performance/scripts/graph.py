from typing import List, Tuple

import matplotlib.dates as mdates
import matplotlib.pyplot as plt


def show_graph(data: List[Tuple[str, float]]):
    year_month_list, rmax_list = zip(*data)

    # Store the axes' data accordingly
    x = mdates.datestr2num(year_month_list)
    y = rmax_list

    # Create a figure and a set of subplots
    fig, ax = plt.subplots()

    # Set the y axis's scale to log2
    ax.set_yscale('log', base=2)

    # Parse the x axis as a date
    ax.xaxis_date()

    # Label the axes
    plt.ylabel('Performance')

    # Display the plot
    plt.plot(x, y)
    plt.show()
