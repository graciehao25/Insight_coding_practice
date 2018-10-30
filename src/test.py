import csv
import sys
from collections import Counter
from get_idx import get_idx
from feature_list import feature_list
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
    filter_idx,features_idx=get_idx(INPUT,filter_str,features_list)

    num_of_entries,list_of_jobs=feature_list(INPUT,filter_idx,filter_condition,features_idx[0])
    num_of_entries,list_of_states=feature_list(INPUT,filter_idx,filter_condition,features_idx[1])
    
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

    rows = [ {output_cols_1[0]:k, output_cols_1[1]:str(v), output_cols_1[2]:"{:.1%}".format(v/float(num_of_entries))} for(k,v) in top_X_occupations]
    with open(OUTPUT0, 'w') as csvfile:
        fp = csv.DictWriter(csvfile, fieldnames = output_cols_1, delimiter=';')
        fp.writeheader()
        fp.writerows(rows)

    rows = [ {output_cols_2[0]:k, output_cols_2[1]:str(v), output_cols_2[2]:"{:.1%}".format(v/float(num_of_entries))} for(k,v) in top_X_states ]
    with open(OUTPUT1, 'w') as csvfile:
        fp = csv.DictWriter(csvfile, fieldnames = output_cols_2, delimiter=';')
        fp.writeheader()
        fp.writerows(rows)

if __name__ == '__main__':
    INPUT = sys.argv[1]
    OUTPUT0 = sys.argv[2]
    OUTPUT1 = sys.argv[3]
    main(INPUT, OUTPUT0, OUTPUT1)



