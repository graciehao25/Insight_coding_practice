import csv
import sys
from collections import Counter
from get_idx import get_idx
from get_feature_list import get_feature_list
from a_list_of_top_X_sorted_feature_dict import a_list_of_top_X_sorted_feature_dict
from write_output_csv import write_output_csv
def main(INPUT, OUTPUT0, OUTPUT1):
    """
    Main function contains six steps:
        1. figure out the column indices of the a list of features 
        2. filter the dataframe by status, create a list for each feature.
        3. Create frequency dictionary for each feature
        4. Sort dictionary by vaule(desc) and alphabet(asc)
        5. crop the dictionary and keep only TOP X
        6. Save the output
    Inputs of the main function:
        1. an INPUT csv file of interests
        2. OUTPUT0 named 'top_10_occupations.txt'
        3. OUTPUT1 named 'top_10_states.txt'
    The main funciton will call two other functions I wrote stored under the src folder:
        1. get_idx to get the indices for the filter variable and features
        2. feature_list to filter the dataframe by status, create a list for each feature.
    """
    # Specs user can customize
    X=10
    filter_str="STATUS"
    filter_condition="CERTIFIED"
    features_list=["SOC_NAME","WORKSITE_STATE"]
    a_list_of_output_paths = [OUTPUT0, OUTPUT1]
    output_cols_1=["TOP_OCCUPATIONS", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE"]
    output_cols_2=["TOP_STATES", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE"]
    output_cols= [output_cols_1,output_cols_2]
    """
    idx in the original data file 
    assuming the filter variable is "STATUS", and st
    get the filter variable index and a list of feature indices
    """
    filter_idx,features_idx=get_idx(INPUT,filter_str,features_list)

    """
    iterate through the list of features user provided in main.py
    """
    num_of_entries, a_list_of_top_x_dicts=a_list_of_top_X_sorted_feature_dict(INPUT,filter_idx,filter_condition,features_idx,X)


    write_output_csv(num_of_entries,a_list_of_top_x_dicts,a_list_of_output_paths)

if __name__ == '__main__':
    INPUT = sys.argv[1]
    OUTPUT0 = sys.argv[2]
    OUTPUT1 = sys.argv[3]
    main(INPUT, OUTPUT0, OUTPUT1)



