import os
import csv

def countVotes(candidates):
    """
        This function counts the number of unique candidates and how many
        votes that they received.

        Input
        -----
        candidates - a list of candidates. 
        Example: ["John", "Doe", "Doe", "Sally"....]

        Ouput
        -----
        electionResults - a dictionary containing the 
        				  candidates and the total number 
                          of votes each one received.
    """   
    electionResults = {} 					# an empty python dictionary
    for can in candidates:
        if can not in electionResults:
            electionResults[can] = 1
        else:
            electionResults[can] += 1
    return electionResults

csvfile = open("Resources/election_data.csv", "r") # open data file
data = csv.reader(csvfile, delimiter = ",")        # have csv parse file
# Next step get the information we care about.
totalVotes = 0              # counter to keep track of number of votes
candidates = []             # a list with all of the candidates
# go through each row and get the candidate that this person voted for
for row in data:
    totalVotes += 1
    candidates.append(row[2])
electionResults = countVotes(candidates[1:])

output = "Analysis"

out_file = open(os.path.join(output, "results.txt"), "w")
print("Election Results")
out_file.write("Election Results\n")
print("-"*50)
out_file.write("-"*50 + "\n")
print("Total Votes: {}".format(totalVotes))
out_file.write("Total Votes: {}\n".format(totalVotes))
print("-"*50)
out_file.write("-"*50 + "\n")
for key in electionResults:
    percentage = round((electionResults[key]/totalVotes)*100,3)
    print("{}: {}% ({})".format(key, percentage, electionResults[key]))
    out_file.write("{}: {}% ({})\n".format(key, percentage, electionResults[key]))
max_value = max(electionResults.values())
for key in electionResults:
    if electionResults[key] == max_value:
        winner = key
print("-"*50)
out_file.write("-"*50 + "\n")
print("Winner: {}".format(winner))
out_file.write("Winner: {}\n".format(winner))
print("-"*50)
out_file.write("-"*50 + "\n")
out_file.close()