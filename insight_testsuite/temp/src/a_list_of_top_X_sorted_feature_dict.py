from get_feature_list import get_feature_list
from collections import Counter
def a_list_of_top_X_sorted_feature_dict(input_file_path,filter_idx,filter_condition,features_idx,X):
    a_list_of_top_X_sorted_feature_dict=[]
    for i in range(len(features_idx)):
        #use self-written function feature_list to filter the dataframe by status, create a list for each feature.
        num_of_entries,flist =get_feature_list(input_file_path,filter_idx,filter_condition,features_idx[i])
        #a_list_of_feature_list.append(feature_list)
        #Create frequency dictionaries
        #feature_count_dict=dict(Counter(a_list_of_feature_list[i]))
        feature_count_dict=dict(Counter(flist))
        #Sort the dictionary by vaule(desc) and alphabet(asc)
        feature_count_dict=sorted(feature_count_dict.items(), key=lambda x: (-x[1],x[0]))
        #a_list_of_feature_count_dict.append(feature_count_dict)
        #crop the dictionary and keep only TOP X
        top_X_feature_dict=feature_count_dict[:X]
        a_list_of_top_X_sorted_feature_dict.append(top_X_feature_dict)

    return num_of_entries, a_list_of_top_X_sorted_feature_dict