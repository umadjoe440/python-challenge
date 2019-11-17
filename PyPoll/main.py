# main.py - PyPoll

import csv
import os
import operator
import locale
from collections import Counter


votes = 0
#vote list will contain a tuple for each row in the input file:
#Voter ID, County, Candidate
vote_list = []
results = []

locale.setlocale( locale.LC_ALL, '')
csvpath = os.path.join("c:/Resources/election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read and print the header row...
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        votes += 1
        vote_list.append((row[2],row[0]))


election_results = Counter(x[0] for x in vote_list)

print("Election Results")
print("-------------------------")
print(f"Total Votes:  {votes}")
print("-------------------------")

highest_vote_count = 0
winner = 'nobody'

for key, value in election_results.items():
    candidate = key
    vote_pct = value/votes
    vote_pct_out = "{:.3%}".format(vote_pct)
    candidate_votes = value
    if candidate_votes > highest_vote_count:
        winner = key
        highest_vote_count = candidate_votes

    print(f"{candidate}: {vote_pct_out} ({candidate_votes})")

print("-------------------------")
print(f"Winner:  {winner}")
print("-------------------------")