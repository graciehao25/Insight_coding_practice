# Insight Data Science Coding Challenge

# Table of Contents
1. [Goal](README.md#goal)
2. [Problem](README.md#problem)
3. [Run Instructions](README.md#run-instructions)
4. [Code Descriptions](README.md#code-descriptions) 
5. [Author](README.md#author)

 
# Goal
This repository provides a solution to the Insight Data Science code challenge. 

The solution python script can be found at https://github.com/graciehao25/Insight_coding_practice/tree/master/src
# Problem
Detailed descripition of the coding challenge can be found here: https://github.com/InsightDataScience/h1b_statistics

# Run Instructions 
## Python Version
The code was tested with Python (v3.6.5).
## How to Start the Program
To run the program, run the `run.sh`. It will evoke the `./src/main.py`.
## Customization 
User can change specifications including **filter criteria**, **features of interests**, and **how many top features to keep** in `./src/main.py`.

# Code Descriptions
## Main Script
Main function contains six steps:
  1. Figure out the column indices of the a list of features 
  2. Filter the dataframe by status, create a list for each feature.
  3. Create frequency dictionary for each feature
  4. Sort dictionary by value (desc) and key alphabet (asc)
  5. Crop the dictionary and keep only TOP X
  6. Save the output

## Inputs of The Main Script

  1. An INPUT csv file of interests
  2. OUTPUT0 named 'top_10_occupations.txt'
  3. OUTPUT1 named 'top_10_states.txt'

## Modules Used
Besides__`csv, sys, collections`__ which are included in python standard distribution, the main funciton will call two other functions I wrote stored under the src folder:
  1. `get_idx.py` to get the indices for the filter variable and features
  2. `feature_list.py` to filter the dataframe by status, create a list for each feature.

## Repo Directory Structure

The directory structure for this repo should is as follows:
```
      └── README.md 
      └── run.sh
      └── src
      │   └──main.py
      │   └──get_idx.py
      │   └──feature_list.py
      └── input
      │   └──h1b_input.csv
      └── output
      │   └── top_10_occupations.txt
      │   └── top_10_states.txt
      └── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
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
