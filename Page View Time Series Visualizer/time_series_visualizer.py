import matplotlib.pyplot as plt
import calendar
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025))
    & (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig = df.plot(kind="line", color='red', legend=False, figsize=(15,5)).figure
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # Adding new columns from date
    df_bar['month'] = df.index.month
    df_bar['year'] = df.index.year

    # Grouping identical values from year and month
    df_bar = df_bar.groupby(['month', 'year'])['value'].mean()

    # Unstacking the dataframe month (index) year (columns)
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = (df_bar).transpose().plot(kind='bar', legend=True, figsize=(15,10)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months",
               labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                       'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)

    df_box['year'] = df.index.year
    df_box["month_num"] = df.index.month
    df_box['month'] = df_box['month_num'].apply(lambda x: calendar.month_abbr[x])

    df_box = df_box.sort_values("month_num")

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.set_figwidth(20)
    fig.set_figheight(10)
    ax1 = sns.boxplot(x=df_box["year"], y=df_box["value"], ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    ax2 = sns.boxplot(x=df_box["month"], y=df_box["value"], ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
