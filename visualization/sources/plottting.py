from pandas import DataFrame
from seaborn import barplot
import matplotlib.pyplot as plt

def plot_pollutant(df:DataFrame):
    y = df.columns[0]
    x = df.columns[1:]
    plt.style.use('seaborn')
    fig = plt.figure(figsize=(12,34))
    for i,j in enumerate(x):
        plt.subplot(len(x),1,i+1)
        barplot(
            data=df,
            x=j,
            y=y,
            orient='h'
        )
        plt.title(f'{j}',fontweight='bold', loc='center')
        plt.xlabel('µg/m³',loc='right')
    fig.tight_layout()
    plt.show()

def plot_stacked_pollutant(df:DataFrame):
    x = df.columns[0]
    y = df.columns[2:]
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(12,8))
    for i,j in enumerate(y):
        ax.barh(
            y=df[x].sort_values(ascending=False),
            width=df[j],
            label=j,
        )
    ax.grid(False, axis='y')
    plt.xlabel('µg/m³', loc='right')
    plt.ylabel(x)
    plt.title('Pollutants per State', fontweight='bold')
    # legend box
    legend = plt.legend(frameon = 1)
    frame = legend.get_frame()
    frame.set_color('white')
    frame.set_facecolor('white')
    frame.set_edgecolor('gray')
    plt.show()