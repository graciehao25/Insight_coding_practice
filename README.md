# H1b_Coding Challenge

# Table of Contents
1. [Goal](README.md#goal)
2. [Problem](README.md#problem)
3. [Approach](README.md#approach) 
4. [Run Instructions](README.md#run-instructions)
5. [Input](README.md#input)
6. [Output](README.md#output)
7. [Repo Directory Structure](README.md#repo-directory-structure)
8. [Author](README.md#author)


# Goal
The repository provides a solution (software code) to the problem described below. 
The solution (software code) is located in the directory src: https://github.com/eachabys/challenge_H1b/tree/master/src. 

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

# Approach

The code was tested with Python (v3.6.5).


# Run Instructions 

# Input 

A .csv data ("h1b_input.csv") used to test the solution to the Problem above is a subset of a Raw dataset(H1B_FY_2014.csv) provided in form of Excel files with a semicolon separated (";") format and placed into this Google drive [folder](https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf?usp=sharing). 
A sample test input data is in the folder 
https://github.com/eachabys/challenge_H1b/tree/master/input
The tests were run on a local machine. 
However changing the input/output fields of the code will produce custom results.



# Output 
The `./src/h1b_counting.py` will generate two txt files:
* `./output/top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `./output/top_10_states.txt`: Top 10 states for certified visa applications

Each line holds one record and each field on each line is separated by a semicolon (;).

Each line of the `top_10_occupations.txt` file contain these fields in this order:
1. __`TOP_OCCUPATIONS`__: The occupation name associated with an application's Standard Occupational Classification (SOC) code. The occupation name corresponds to the "SOC_NAME" field in the header of the input file.
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for that occupation. An application is considered certified if it has a case status of `CERTIFIED`
3. __`PERCENTAGE`__: % of applications that have been certified for that occupation compared to total number of certified applications regardless of occupation. 

The records in the ouput files are sorted by __`NUMBER_CERTIFIED_APPLICATIONS`__, and in case of a tie, alphabetically by __`TOP_OCCUPATIONS`__.

Each line of the `top_10_states.txt` file contain these fields in this order:
1. __`TOP_STATES`__: State where the work will take place. The state corresponds to "WORKSITE_STATE" field in the header of the input file.
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for work in that state. An application is considered certified if it has a case status of `CERTIFIED`
3. __`PERCENTAGE`__: % of applications that have been certified in that state compared to total number of certified applications regardless of state.

The records in this file are sorted by __`NUMBER_CERTIFIED_APPLICATIONS`__ field, and in case of a tie, alphabetically by __`TOP_STATES`__. 

Percentages is rounded to 1 decimal. 

# Repo Directory Structure

The directory structure for your repo should look like this:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_topmetrics.py
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── texts
              └── text_1
              |   └── input
              |   |   └──h1b_input.csv
              |   └── output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              └── Gracie_test_1
                  └── input
                  |   └──h1b_input.csv
                  └── output
                  |   └── top_10_occupations.txt
                  |   └── top_10_states.txt

```
# Author

Hui (Gracie) Hao, Ph.D. Candidate, Department of Economics, Vanderbilt University, Nashville, TN, USA.

Email: hui.hao@vanderbilt.edu and graciehao25@gmail.com
LinkedIn: https://www.linkedin.com/in/gracie-hao-5b46a564/
