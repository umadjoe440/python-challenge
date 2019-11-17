# main.py - PyPoll

import csv
import os
from collections import Counter


votes = 0
# vote list will contain a tuple for each row in the input file:
#Candidate, Voter ID
vote_list = []

csvpath = os.path.join("c:/Resources/election_data.csv")
outpath = os.path.join("c:/Resources/election_results.txt")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read and print the header row...
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        votes += 1
        vote_list.append((row[2],row[0]))

#Create counter to count votes by candidate
election_results = Counter(x[0] for x in vote_list)

results_file = open(outpath, "w")

print("Election Results")
print("-------------------------")
print(f"Total Votes:  {votes}")
print("-------------------------")

results_file.write("Election Results\n")
results_file.write("-------------------------\n")
results_file.write(f"Total Votes:  {votes}\n")
results_file.write("-------------------------\n")

highest_vote_count = 0
winner = 'nobody'


# loop through counter to print results and determine winner
for key, value in election_results.items():
    candidate = key
    vote_pct = value/votes
    vote_pct_out = "{:.3%}".format(vote_pct)
    candidate_votes = value
    if candidate_votes > highest_vote_count:
        winner = key
        highest_vote_count = candidate_votes

    print(f"{candidate}: {vote_pct_out} ({candidate_votes})")
    results_file.write(f"{candidate}: {vote_pct_out} ({candidate_votes})\n")

print("-------------------------")
print(f"Winner:  {winner}")
print("-------------------------")

results_file.write("-------------------------\n")
results_file.write(f"Winner:  {winner}\n")
results_file.write("-------------------------\n")