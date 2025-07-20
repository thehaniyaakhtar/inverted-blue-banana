import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit (all data)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(1880, 2051))
    y1 = res1.intercept + res1.slope * x1
    plt.plot(x1, y1, 'r', label='Fit: 1880–2050')

    # Create second line of best fit (from year 2000)
    df_2000 = df[df['Year'] >= 2000]
    res2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = res2.intercept + res2.slope * x2
    plt.plot(x2, y2, 'g', label='Fit: 2000–2050')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save and return plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
