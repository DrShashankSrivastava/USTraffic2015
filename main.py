"""
Main file for US Traffic 2015 dataset challenge for OCBS Hack-IT 2021
Data & AI Track
"""
# Import libraries
from data_preprocessing import read_csv_data

# Datafile source directory and filename
src = r'/Users/shashank/Documents/ocbc'
filename_traffic = r'dot_traffic_2015.txt'
filename_stations = r'dot_traffic_stations_2015.txt'
raw_traffic = read_csv_data(src, filename_traffic)
raw_stations = read_csv_data(src, filename_stations)

# Garbage collection
del src, filename_stations, filename_traffic
