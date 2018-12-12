# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

calendar = []
dollar_value = []
#average_change = []
csvpath = os.path.join('', 'Resources', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:

   # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

   # Read the header row first (skip this step if there is now header)
   csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

   # Read each row of data after the header
   for row in csvreader:
       calendar.append(row[0])
       value = int(row[1])
       max_dollar_value = int(row[1])
       changed_value = int(row[1]) - int(row[1])+1
       dollar_value.append(value)
    
month = len(calendar)
total = sum(dollar_value)
#max_value = max(dollar_value)
#min_value = min(dollar_value)
#print(month)
#print(total)
print(changed_value)





print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month))
print("Total: $" + str(total))
print("Average Change: ")
print("Greatest Increase in Profits: " + str(max(dollar_value)))
print("Greatest Decrease in Profits: " + str(min(dollar_value)))


# Print results
#print("The total numbers of months included in the dataset is " + str(total_months) + " months!")
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

