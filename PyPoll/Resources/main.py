# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv
from pathlib import Path
import math

#open('/Users/fatimadonato/Desktop/python-challenge/PyPoll/Resources/PyPoll.csv')
csvpath = os.path.join('PyPoll.csv')

with open(csvpath) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    TotalVotes=0
    Candidates= {}
    percentVote =[]

    # Read each roWITHw of data after the header
    for row in csv_reader:
        if row[2] not in Candidates.keys():
            Candidates[row[2]]= 1
            
        else:
            Candidates[row[2]]= Candidates[row[2]] + 1
        TotalVotes= TotalVotes + 1  

print(Candidates, TotalVotes)

# Specify the file to write to
output_path = os.path.join("..", "Analysis", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w+') as csvfile:
    winner= ""
    Votes= 0

    csvfile.write("Election Results\n")
    csvfile.write("-"*30+"\n")
    csvfile.write(f"Total Votes:{TotalVotes}\n")
    csvfile.write("-"*30+"\n")
    for x, value in Candidates.items():
        if value> Votes:
            winner = x
            Votes = value
        percentVote = round((value/TotalVotes) * 100, 1)
        csvfile.write(f" {x} : {percentVote}% ({value})\n")
    csvfile.write("-"*30+"\n")
    csvfile.write(f"Winner: {winner}\n")
    csvfile.write("-"*30+"\n")
     
#winner  




