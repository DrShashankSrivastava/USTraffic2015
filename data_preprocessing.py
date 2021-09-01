"""
"""
# Library imports
import os

def read_csv_data(src_path: 'str', filename: 'str') -> list:
    file_path = os.path.join(src_path, filename)
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    return lines
