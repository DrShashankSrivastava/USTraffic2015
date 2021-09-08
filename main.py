"""
Main file for US Traffic 2015 dataset challenge for OCBS Hack-IT 2021
Data & AI Track
"""
# Import libraries
import pandas as pd

from data_preprocessing import read_raw_data

# Datafile source directory and filename
src = r'/Users/shashank/Documents/ocbc'

filename_traffic = r'dot_traffic_2015.txt'
filename_stations = r'dot_traffic_stations_2015.txt'

# Keeping first 100 rows only
raw_traffic = read_raw_data(src, filename_traffic)[:100]
raw_stations = read_raw_data(src, filename_stations)[:100]

# Garbage collection
del src, filename_stations, filename_traffic

raw_traffic.to_csv(r'/Users/shashank/Documents/ocbc/raw_traffic_100.csv')
raw_stations.to_csv(r'/Users/shashank/Documents/ocbcraw_stations_100.csv')