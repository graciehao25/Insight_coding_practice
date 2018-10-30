# Insight Data Science Coding Challenge

# Table of Contents
1. [Goal](README.md#goal)
2. [Problem](README.md#problem)
3. [Run Instructions](README.md#run-instructions)
4. [Code Descriptions](README.md#code-descriptions) 
5. [Author](README.md#author)


# Goal
The repository provides a solution (software code) to the problem described below. 
The solution (software code) is located in the directory src: https://github.com/eachabys/challenge_H1b/tree/master/src. 

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 


# Run Instructions 
## python version
The code was tested with Python (v3.6.5).
## How to start the programs
To run the program, run the `run.sh`. It will evoke the `./src/main.py`.
## Customization 
User can change the _filter criteria_, _features of interests_, and _how many top features to keep_ in `./src/main.py`.

# Code Descriptions
## Main Function
Main function contains six steps:
    1. figure out the column indices of the a list of features 
    2. filter the dataframe by status, create a list for each feature.
    3. Create frequency dictionary for each feature
    4. Sort dictionary by vaule(desc) and alphabet(asc)
    5. crop the dictionary and keep only TOP X
    6. Save the output

##Inputs of the main function
Inputs of the main function:
    1. an INPUT csv file of interests
    2. OUTPUT0 named 'top_10_occupations.txt'
    3. OUTPUT1 named 'top_10_states.txt'

## Modules Used
Besides__`csv, sys, collections`__ which are included in python standard distribution, the main funciton will call two other functions I wrote stored under the src folder:
    1. get_idx to get the indices for the filter variable and features
    2. feature_list to filter the dataframe by status, create a list for each feature.

## Repo Directory Structure

The directory structure for this repo should is as follows:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──main.py
      │   └──get_idx.py
      │   └──feature_list.py
      ├── input
      │   └──h1b_input.csv
      ├── output
      │   └── top_10_occupations.txt
      │   └── top_10_states.txt
      │── insight_testsuite
          └── run_tests.sh
          └── tests
              │── test_1
              │   └── input
              │   |   └──h1b_input.csv
              │   └── output
              │       └── top_10_occupations.txt
              │       └── top_10_states.txt
              └── Gracie_test_1
                  └── input
                  |   └──h1b_input.csv
                  └── output
                      └── top_10_occupations.txt
                      └── top_10_states.txt

```
# Author

Hui (Gracie) Hao, Ph.D. Candidate, Department of Economics, Vanderbilt University, Nashville, TN, USA.

Email: hui.hao@vanderbilt.edu and graciehao25@gmail.com

LinkedIn: https://www.linkedin.com/in/gracie-hao-5b46a564/
