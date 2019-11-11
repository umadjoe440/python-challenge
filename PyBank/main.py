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
