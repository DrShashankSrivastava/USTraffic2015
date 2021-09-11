"""
Main file for US Traffic 2015 dataset challenge for OCBS Hack-IT 2021
Data & AI Track
"""
#%% Import libraries
# <editor-fold desc="Import Libraries">
import pandas as pd
import numpy as np
from data_preprocessing import read_raw_data
# </editor-fold>

#%% Datafile source directory and filename
# <editor-fold desc="Datafile source directory and filename">
src = r'/Users/shashank/Documents/ocbc'

filename_traffic = r'dot_traffic_2015.txt'
filename_stations = r'dot_traffic_stations_2015.txt'

# Keeping first 100 rows only
raw_traffic = read_raw_data(src, filename_traffic)
raw_stations = read_raw_data(src, filename_stations)

# Garbage collection
del src, filename_stations, filename_traffic
# </editor-fold>

#%% Inspect raw_traffic dataset
# <editor-fold desc="Inspect raw_traffic dataset">
for col in raw_traffic.columns:
    print(col)

print(raw_traffic.head())

# Check if 'restrictions' columns has any value
print(np.unique(raw_traffic['restrictions']))

# Drop reduntant or empty columns
raw_traffic = raw_traffic.drop(columns=['date', 'direction_of_travel_name', 
                                'functional_classification_name', 'restrictions'])
# </editor-fold>

## Raw_traffic: Datatype conversion to numeric values
# <editor-fold desc="Datatype conversion to numeric values">
for col in raw_traffic.columns:
    if col not in ['functional_classification', 'station_id']:
        raw_traffic[col] = pd.to_numeric(raw_traffic[col], errors='coerce')
# </editor-fold>

#%% Inspect raw_station dataset
# <editor-fold desc="Inspect raw_stations dataset">
for col in raw_stations.columns:
    print(col)

print(raw_stations.head())

# </editor-fold>
