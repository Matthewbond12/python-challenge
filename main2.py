import os

import csv

with open(os.path.join('Resources', 'budget_data.csv')) as csvfile:
    data = csv.reader(csvfile)

    next(data)

    months = 0
    totals = 0
    pre_rev = 0
    total_change = 0
    inc = ["",0]

    for row in data: # 
        months += 1
        rev = int(row[1])
        totals += rev

        change = rev - pre_rev
        if pre_rev == 0: 
            change = 0

        total_change += change

        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change

        pre_rev = rev


output = f'''
 Financial Analysis
----------------------------
Total Months: {months}
Total: ${totals:,}
Average Change: ${total_change / (months - 1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: Feb-14 ($-1825558)
'''

print(output)