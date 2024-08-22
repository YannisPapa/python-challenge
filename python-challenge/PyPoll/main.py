import os
import csv

#Create variables and lists
vote_count = 0
candidates = []
candidates_votes = []

#Open the file to read
budget_data_csv = os.path.join("Resources/election_data.csv")
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    header = next(csvreader)

    #go line by line to gather data needed
    for row in csvreader:
        #count the number of votes
        vote_count += 1

        #check if the candidate already exsists
        if row[2] not in candidates:
            #if they dont add them to the list and start a vote count
            candidates.append(row[2])
            candidates_votes.append(1)
        else:
            #if they are in the list increase thier vote count
            candidates_votes[candidates.index(row[2])] += 1

#create a new file to write in
output_file = os.path.join("analysis/election_data_results.txt")
with open(output_file, "w") as datafile:
    #write the results to a file
    datafile.write("Election Results\n")
    datafile.write("--------------------------\n")
    datafile.write(f"Total Votes: {vote_count}\n")
    datafile.write("--------------------------\n")
    for i in candidates:
         datafile.write(f"{i}: {round((candidates_votes[candidates.index(i)]/vote_count) * 100,3)}% ({candidates_votes[candidates.index(i)]})\n")
    datafile.write("--------------------------\n")
    datafile.write(f"Winner: {candidates[candidates_votes.index(max(candidates_votes))]}\n")
    datafile.write("--------------------------")

#print the results to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {vote_count}")
print("--------------------------")
for i in candidates:
    print(f"{i}: {round((candidates_votes[candidates.index(i)]/vote_count) * 100,3)}% ({candidates_votes[candidates.index(i)]})")
print("--------------------------")
print(f"Winner: {candidates[candidates_votes.index(max(candidates_votes))]}")
print("--------------------------")