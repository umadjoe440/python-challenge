# main.py - PyBank

import csv
import os

csvpath = os.path.join("c:/Resources/00-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read and print the header row...
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    row_list = []
    months = 0
    total_money = 0
    for row in csvreader:
        months += 1
        total_money += float(row[1])
        row_list.append((row[0],row[1]))
        # The total number of months included in the dataset
        # The net total amount of "Profit/Losses" over the entire period
        # The average of the changes in "Profit/Losses" over the entire period
        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in losses (date and amount) over the entire period

    print(f"The total number of months is:  {months}")
    print(f"The total money is:  {total_money}")
