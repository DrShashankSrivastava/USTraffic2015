"""
"""
# Library imports
import os
from pandas import DataFrame

def read_raw_data(src_path: 'str', filename: 'str') -> DataFrame:
    file_path = os.path.join(src_path, filename)
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data_list = f.readlines()
    columns = data_list[0].split(',')
    data = []
    # for i in range(1, len(data_list)):
    for i in range(1, 100):
        data.append(data_list[i].split(','))
    df = DataFrame(data = data, columns = columns)
    return df
