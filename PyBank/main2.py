#Import Dependencies

import os

import csv

# Determine file path and store in new variable for CSV file
with open(os.path.join(r"C:\Users\matth\OneDrive\Desktop\python-challenge\Resources\budget_data.csv")) as csvfile:
    budget_data = csv.reader(csvfile)

    next(budget_data)
# Create and assign variables    
    months = 0
    totals = 0
    pre_rev = 0
    total_change = 0
#Assign and create increasing and decreasing variables storing first column and second column values
    inc = ["",0]
    dec = ["",99999999999999999]
#Loop through every row in the dataset adding totals for months and rev
    for row in budget_data: # 
        months += 1
        rev = int(row[1])
        totals += rev
#Define variable to store delta between revenue and pre-revenue variables        
        change = rev - pre_rev
#Set condition to aggregate the delta between revenue and pre-revenue variables         
        if pre_rev == 0: 
            change = 0

        total_change += change
#Set condition to evaluate if new increasing change max is greater than next row change max
        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change

        pre_rev = rev
#Set condition to evaluate if new decreasing change min is less than next row change min
        if change < dec[1]:
            dec[0] = row[0]
            dec[1] = change

# Copied summary analysis string and print
output = f'''
 Financial Analysis
----------------------------
Total Months: {months}
Total: ${totals:,}
Average Change: ${total_change / (months - 1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''

print(output)

#Designate the file path to write to
with open(r"C:\Users\matth\OneDrive\Desktop\python-challenge\Analysis\pybank_output.txt", "w", encoding='utf-8') as output_file :

    output_file.write(output)
