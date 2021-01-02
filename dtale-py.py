import dtale
import os
from pathlib import Path
import pandas as pd

data_path = Path( os.getcwd(), 'data/kraken/COMPUSD.csv' ) 

print(data_path)

data = pd.read_csv( data_path )

print( type(data) )

# Assigning a reference to a running D-Tale process
d = dtale.show( data )