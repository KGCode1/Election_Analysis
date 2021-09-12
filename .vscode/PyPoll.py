#1. Import data file
#2. Total number of votes cast
#3. Get the list of candidates
#4. Total number of votes for each candidate
#5. % of total votes each candidate won
#6. The populat vote winner of the election

import datetime as dt 
now = dt.datetime.today()

# Print current time

print(f" Current time is {now}")

import csv 
import random
import numbers
import os

#1.Import data file

#file_to_load = 'Resources/election_results.csv'

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_results.txt")

with open(file_to_load) as election_data:
    # Read the election results file
    file_read = csv.reader(election_data)
    #read the headers from file
    headers = next(file_read)
    #Print headers
    print(headers)

    i=0
    while i<5:
        for row in file_read:
            print(row)
            i=i+1


# Create variable to save the results to text file



with open(file_to_save,"w") as results:
    #print(results)
    results.write(f"Time of counting : {now}\n")
    results.write("List of counties:\n")
    results.write("--------------------\n")
    results.write("Arapahoe\n")
    results.write("Denver\n")
    results.write("Jefferson\n")




