import csv
def write_output_csv(num_of_entries,a_list_of_top_X_sorted_feature_dict,a_list_of_output_paths):

    output_cols_1=["TOP_OCCUPATIONS", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE"]
    output_cols_2=["TOP_STATES", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE"]
    output_cols= [output_cols_1,output_cols_2]

    for i in range(len(a_list_of_top_X_sorted_feature_dict)):
        rows = [ {output_cols[i][0]:k, output_cols[i][1]:str(v), output_cols[i][2]:"{:.1%}".format(v/float(num_of_entries))} for(k,v) in a_list_of_top_X_sorted_feature_dict[i]]
        with open(a_list_of_output_paths[i], 'w') as csvfile:
            fp = csv.DictWriter(csvfile, fieldnames = output_cols[i], delimiter=';')
            fp.writeheader()
            fp.writerows(rows)

