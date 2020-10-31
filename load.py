# Reads csv data

from pathlib import Path
from os import getcwd
import pandas as pd
import numpy as np


# objects
from objects.parameters import COLS


# Reads from a csv file
def read_data( data_path : Path, file_name: str, column_headers: list ):
    '''
        data_path: Path where the data is located
        file_name: name of the file
        column_headers: headers to label each column
    '''

    data = pd.read_csv( Path(data_path, file_name), header=None, names=column_headers )

    # print( data.groupby( 'TIME' )[ 'PRICE' ].value_counts( normalize=True ) )
    
    # print( data.groupby( 'PRICE' )[ 'TIME' ].mean() )

    # print( data.corr() )

    # data[ 'high_price' ] = data.PRICE.apply(lambda x: x > 200 )
    # print ( data.corr() )

    # print( data.describe( percentiles=[ .05, .1, .5, .9, .95 ] ) )

    # pivot_table = pd.pivot_table( data, values='PRICE', index=[ 'TIME' ], columns=[ 'TIME' ], aggfunc=np.mean)
    # print( pivot_table )

    return data.head(), data.describe(), data.info

def group_by( data_path : Path, file_name: str, column_headers: list ):

    data = pd.read_csv( Path(data_path, file_name), header=None, names=column_headers )


if __name__ == '__main__':

    data_path = Path( getcwd() , 'data/kraken')
    file_name = 'COMPUSD.csv'

    head, describe, info = read_data( data_path=data_path, file_name=file_name, column_headers=COLS.values() )


