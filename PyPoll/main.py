# main.py - PyPoll

import csv
import os
import operator
import locale

locale.setlocale( locale.LC_ALL, '')
csvpath = os.path.join("c:/Resources/election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read and print the header row...
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

