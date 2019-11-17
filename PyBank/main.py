# main.py - PyBank

import csv
import os
import operator

csvpath = os.path.join("c:/Resources/budget_data.csv")
outpath = os.path.join("c:/Resources/budget_report.txt")

# open budget data file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    row_list = []
    monthly_list = []
    months = 0
    total_money = 0
    for row in csvreader:
        months += 1
        total_money += float(row[1])
        row_list.append((row[0],row[1]))
        
    #JGP generate another list of tuples with month and monthly profit/loss
    for r in row_list:
        if row_list.index(r) == 0:
            start_profit = float(r[1])
        else:
            end_profit = float(r[1])
            monthly_diff = end_profit - start_profit
            monthly_list.append((r[0],monthly_diff))
            start_profit = end_profit
            

    #open report file for writing    
    report_file = open(outpath, "w")

    print("Financial Analysis")
    print("----------------------------")
    print()

    report_file.write("Financial Analysis\n")
    report_file.write("----------------------------\n")
    report_file.write("\n")


    # The total number of months included in the dataset
    print(f"Total Months:  {months}")
    report_file.write(f"Total Months:  {months}\n")
    # The net total amount of "Profit/Losses" over the entire period
    total_money_out = "${:0.0f}".format(total_money)
    print(f"Total:  {total_money_out}")
    report_file.write(f"Total:  {total_money_out}\n")
    

    #calculate average
    sum_monthly_changes = sum([m[1] for m in monthly_list])
    average_change = sum_monthly_changes/len(monthly_list)
    average_change_out = "${:0.2f}".format(average_change)
    print(f"Average Change:  {average_change_out}")
    report_file.write(f"Average Change:  {average_change_out}\n")

    #greatest increase and decrease
    greatest_increase_month = max(monthly_list,key=operator.itemgetter(1))[0]
    greatest_increase_amount = max(monthly_list,key=operator.itemgetter(1))[1]
    greatest_increase_out = "${:0.0f}".format(greatest_increase_amount)
    greatest_decrease_month = min(monthly_list,key=operator.itemgetter(1))[0]
    greatest_decrease_amount = min(monthly_list,key=operator.itemgetter(1))[1]
    greatest_decrease_out = "${:0.0f}".format(greatest_decrease_amount)

    print(f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase_out})")
    print(f"Greatest Decrease in Profits: {greatest_increase_month} ({greatest_decrease_out})")

    report_file.write(f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase_out})\n")
    report_file.write(f"Greatest Decrease in Profits: {greatest_increase_month} ({greatest_decrease_out})\n")