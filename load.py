# Reads csv data

# helper libraries
from pathlib import Path
from os import getcwd

# data libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# objects
from objects.parameters import COLS

# globals
data_path = Path( getcwd() , 'data/kraken')
file_name = 'COMPUSD.csv'


# Reads from a csv file
def read_data( data_path : Path, file_name: str, column_headers: list ):
    '''
        data_path: Path where the data is located
        file_name: name of the file
        column_headers: headers to label each column
    '''

    data = pd.read_csv( Path(data_path, file_name), header=None, names=column_headers )

    return data

# Plots an sns scatter plot from the data object
def plot_scatter( data: pd.DataFrame, x: str, y: str ):
    '''
        data: pandas DataFrame being analyzed
        x: x-axis variable plot
        y: y-axis variable plot
    '''

    # creates the scatter plot
    sns.lmplot( x=x, y=y, data=data )

    # removes excess chart lines and ticks for a nice looking plot
    # sns.despine()

    # shows the scatter plot
    plt.show()


if __name__ == '__main__':

    data = read_data( data_path=data_path, file_name=file_name, column_headers=COLS.values() )

    plot_scatter( data=data, x='TIME', y='PRICE' )


