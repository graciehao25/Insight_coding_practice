
import csv
import sys


def get_idx(input_file_path,filter_str,features_list):
    features_idx=[]
    with open(input_file_path) as csv_file: 
        reader=csv.DictReader(csv_file,delimiter=";")
        col_names = reader.fieldnames
        for col_name in col_names:
            if col_name.endswith(filter_str):
                filter_idx = col_names.index(col_name)
        for feature in features_list:
            for col_name in col_names:
                if col_name.endswith(feature):
                    features_idx.append(col_names.index(col_name))
    return filter_idx,features_idx