
import csv
import sys
import glob
import operator
from collections import Counter

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

def feature_list(input_file_path,filter_idx,filter_condition, feature_idx):
    """
    filter the dataframe by status, create a list for each feature.

    """
    list_of_feature=[]
    lines=0
    with open(input_file_path) as csv_file: 
        reader = csv.reader(csv_file,delimiter=';')
        filtered_df = filter(lambda col: filter_condition == col[filter_idx], reader)
        # row is a list of strings; 
        for row in filtered_df:
            lines += 1
            # row[24] is the str indicates the job title
            list_of_feature.append(row[feature_idx]) 
    return list_of_feature

def main(INPUT, OUTPUT0, OUTPUT1):
    """
    The main funciton will 
    Main function contains three steps:
    1. figure out the column indices of the a list of features 
    2. filter the dataframe by status, create a list for each feature.
    3. Create frequency dictionary for each feature
    4. Sort dictionary by vaule(desc) and alphabet(asc)
    5. crop the dictionary and keep only TOP X
    6. Save the output
    """
    X=10
    filter_str="STATUS"
    filter_condition="CERTIFIED"
    features_list=["SOC_NAME","WORKSITE_STATE"]
    """
    assuming the filter variable is "STATUS", and st
    get the filter variable index and a list of feature indices
    """
    get_idx(INPUT,filter_str,features_list)

    list_of_jobs=feature_list(INPUT,2,filter_condition,24)
    list_of_states=feature_list(INPUT,2,filter_condition,50)
    num_of_entries=10
    #Create frequency dictionaries
    job_count_dict=dict(Counter(list_of_jobs))
    state_count_dict=dict(Counter(list_of_states))
    #Sort the dictionary by vaule(desc) and alphabet(asc)
    state_count_dict=sorted(state_count_dict.items(), key=lambda x: (-x[1],x[0]))
    job_count_dict=sorted(job_count_dict.items(), key=lambda x: (-x[1],x[0]))
    # a list of tuples like [('FL', 2), ('AL', 1),...]
    top_X_states=state_count_dict[:X]
    # a list of tuples like [('SOFTWARE DEVELOPERS, APPLICATIONS', 6),...]
    top_X_occupations=job_count_dict[:X]
    #create an empty list of tuples [(job, counts, %)]

    outputs = [OUTPUT0, OUTPUT1]
    output_cols_1=["TOP_OCCUPATIONS", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE"]
    output_cols_2=["TOP_STATES", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE"]
    output_cols= [output_cols_1,output_cols_2]

    rows = [ {output_cols_1[0]:k, output_cols_1[1]:str(v), output_cols_1[2]:"{:.1%}".format(v/float(10))} for(k,v) in top_X_occupations ]
    with open(OUTPUT0, 'w') as csvfile:
        fp = csv.DictWriter(csvfile, fieldnames = output_cols_1, delimiter=';')
        fp.writeheader()
        fp.writerows(rows)

    rows = [ {output_cols_2[0]:k, output_cols_2[1]:str(v), output_cols_2[2]:"{:.1%}".format(v/float(10))} for(k,v) in top_X_states ]
    with open(OUTPUT1, 'w') as csvfile:
        fp = csv.DictWriter(csvfile, fieldnames = output_cols_2, delimiter=';')
        fp.writeheader()
        fp.writerows(rows)

if __name__ == '__main__':
    INPUT = sys.argv[1]
    OUTPUT0 = sys.argv[2]
    OUTPUT1 = sys.argv[3]
    main(INPUT, OUTPUT0, OUTPUT1)



