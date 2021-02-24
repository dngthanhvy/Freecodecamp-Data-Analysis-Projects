import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df_scatter = df.copy()
    df_scatter.plot(kind="scatter", x='Year', y='CSIRO Adjusted Sea Level', figsize=(15, 5), label='data')

    # Create first line of best fit
    df_linregress = linregress(df_scatter['Year'], df_scatter['CSIRO Adjusted Sea Level'])
    plt.plot(df_scatter['Year'], df_linregress.slope * df_scatter['Year'] + df_linregress.intercept, 'r',
                   label='fitted line')

    # Create second line of best fit
    df_2000 = df.copy()
    df_2000 = df_2000[df_2000['Year'] >= 2000]
    df_linregress2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    new2000to2050 = pd.Series([int(i) for i in range(2000, 2051)])
    plt.plot(new2000to2050, df_linregress2.slope*new2000to2050 + df_linregress2.intercept, 'g', label='2050 fitted line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
