# main.py - PyBank

import csv
import os
import operator

csvpath = os.path.join("c:/Resources/budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read and print the header row...
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    row_list = []
    monthly_list = []
    months = 0
    total_money = 0
    for row in csvreader:
        months += 1
        total_money += float(row[1])
        row_list.append((row[0],row[1]))
        
        # The average of the changes in "Profit/Losses" over the entire period
        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in losses (date and amount) over the entire period
    for r in row_list:
        if row_list.index(r) == 0:
            start_profit = float(r[1])
        else:
            end_profit = float(r[1])
            #print(f"end_profit {end_profit} start profit {start_profit}")
            monthly_diff = end_profit - start_profit
            monthly_list.append((r[0],monthly_diff))
            start_profit = end_profit
            
    # using min() and max() 
# to get min and max in list of tuples 
    #JGP generate another list of tuples with month and monthly profit/loss
    #JGP then run the below function against the new list
    #res1 = min(test_list)[0], max(test_list)[0] 
    #res2 = min(test_list)[1], max(test_list)[1] 

    print("Financial Analysis")
    print("----------------------------")
    print()

    # The total number of months included in the dataset
    print(f"Total Months:  {months}")
    # The net total amount of "Profit/Losses" over the entire period
    print(f"Total: $ {total_money}")
    #print(monthly_list)

    #calculate average
    sum_monthly_changes = sum([m[1] for m in monthly_list])
    average_change = sum_monthly_changes/len(monthly_list)
    print(f"Average Change:  {average_change}")

    #greatest increase and decrease
    greatest_increase_month = max(monthly_list,key=operator.itemgetter(1))[0]
    greatest_increase_amount = max(monthly_list,key=operator.itemgetter(1))[1]
    greatest_decrease_month = min(monthly_list,key=operator.itemgetter(1))[0]
    greatest_decrease_amount = min(monthly_list,key=operator.itemgetter(1))[1]

    print(f"Greatest Increase in Profits: {greatest_increase_month} {greatest_increase_amount}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} {greatest_decrease_amount}")

    for month in monthly_list:
        print(month)