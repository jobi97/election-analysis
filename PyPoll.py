
#add dependencies
import csv
import os
#assign a variable for the file 
'election-analysis/election_results.csv'
election_data = open('election-analysis/election_results.csv', 'r') 

# Create a filename variable for outfile
outfile = open('election-analysis/analysis/election_analysis.txt', 'w')

#to do, read and analyze the data
file_reader = csv.reader(election_data)

headers = next(file_reader)
print(headers)