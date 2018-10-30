import csv
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
    return lines,list_of_feature