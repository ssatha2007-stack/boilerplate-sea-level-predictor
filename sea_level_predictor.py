import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import the data
    df = pd.read_csv("epa-sea-level.csv")

    # Create the scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Calculate the line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create years from the first year in the dataset through 2050
    years = range(df["Year"].min(), 2051)

    # Calculate predicted sea levels
    predicted_sea_level = slope * years + intercept

    # Plot the line of best fit
    plt.plot(
        years,
        predicted_sea_level,
        label="Line of best fit"
    )

    # Filter data from the year 2000 onwards
    df_recent = df[df["Year"] >= 2000]

    # Calculate the line of best fit using data from 2000 onwards
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Create years from 2000 through 2050
    recent_years = range(2000, 2051)

    # Calculate predicted sea levels for recent data
    recent_predicted_sea_level = (
        slope_recent * recent_years + intercept_recent
    )

    # Plot the second line of best fit
    plt.plot(
        recent_years,
        recent_predicted_sea_level,
        label="Line of best fit from 2000"
    )

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save the plot
    plt.savefig("sea_level_plot.png")

    # Return the plot
    return plt.gca()