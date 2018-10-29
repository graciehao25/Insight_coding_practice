#Beginning of the file 
############################################################
#Hui (Gracie) Hao Insight Data Science Coding Challenge  
# hui.hao@vanderbilt.edu
# Phone: 615-818-9228
# Oct. 29th, 2018
############################################################
# Import Modules
import csv
import sys
import glob
import operator
from collections import Counter
#create empty lists
list_of_jobs=[]
list_of_states=[]
lines=0
#read a 'list of jobs' and a 'list of states'
with open("h1b_input.csv") as csv_file: 
    reader = csv.reader(csv_file,delimiter=';')
    filtered_df = filter(lambda col: 'CERTIFIED' == col[2], reader)
    # row is a list of strings; 
    for row in filtered_df:
        lines += 1
        # row[24] is the str indicates the job title
        list_of_jobs.append(row[24]) 
        # row[50] is the str indicates the state
        list_of_states.append(row[50]) 
            #list_of_jobs+= job
#Create frequency dictionaries
job_count_dict=dict(Counter(list_of_jobs))
state_count_dict=dict(Counter(list_of_states))
#Sort the dictionary by vaule(desc) and alphabet(asc)
state_count_dict=sorted(state_count_dict.items(), key=lambda x: (-x[1],x[0]))
job_count_dict=sorted(job_count_dict.items(), key=lambda x: (-x[1],x[0]))
# a list of tuples like [('FL', 2), ('AL', 1),...]
top_10_states=state_count_dict[:10]
# a list of tuples like [('SOFTWARE DEVELOPERS, APPLICATIONS', 6),...]
top_10_occupations=job_count_dict[:10]
#create an empty list of tuples [(job, counts, %)]
top_10_occupations_triplets=[('TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE')]
for(k,v)in top_10_occupations:
    top_10_occupations_triplets.append((k,v,v/lines))
#create an empty list of tuples [(state, counts, %)]
top_10_states_triplets=[('TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE')]
for(k,v)in top_10_states:
    top_10_states_triplets.append((k,v,v/lines))   
# write top_10_states.txt
states_file = open('top_10_states.txt', 'w')
for triplet in top_10_states_triplets:
    line = ';'.join(str(x) for x in triplet)
    states_file.write(line + ';\n')
states_file.close()
# write top_10_occupations.txt
jobs_file = open('top_10_occupations.txt', 'w')
for triplet in top_10_occupations_triplets:
    line = ';'.join(str(x) for x in triplet)
    jobs_file.write(line + ';\n')
jobs_file.close()

