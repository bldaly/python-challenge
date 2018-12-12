# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

number_votes = []
voter_id = []
candidate_votes = []
#average_change = []
csvpath = os.path.join('', 'Resources', 'election_data.csv')


with open(csvpath, newline='') as csvfile:

   # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

   # Read the header row first (skip this step if there is now header)
   csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

   # Read each row of data after the header
   for row in csvreader:
       voter_id.append(row[0])
       #value = int(row[1])
       #dollar_value.append(value)
    
#Re-do this section
total_votes = int(len(number_votes))
#total = sum(dollar_value)
#max_value = max(dollar_value)
#min_value = min(dollar_value)
#print(month)
#print(total)
#print(max_value)





print("Election Results")
print("----------------------------")
print("Total votes: " + len(number_votes))
print("Khan: ")
print("Correy: ")
print("Li: ")
print("O'Tooley: ")
print("----------------------------")
print("Winner:" )



