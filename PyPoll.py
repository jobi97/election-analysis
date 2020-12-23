
#add dependencies
import csv
import os
#assign a variable for the file 
'election-analysis/election_results.csv'
election_data = open('election-analysis/election_results.csv', 'r') 

# Create a filename variable for outfile
outfile = open('election-analysis/analysis/election_analysis.txt', 'w')

# Initialize a total vote counter.
total_votes = 0
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#candidate options
candidate_options = []

#create empty dictionary
candidate_votes ={}
#to do, read and analyze the data
file_reader = csv.reader(election_data)

# read the header row
headers = next(file_reader)

#print each row in csv file
for row in file_reader:
    #add to the total vote count
    total_votes +=1
    
    #print the candidate name from each row
    candidate_name = row[2]
    #we only want unique candidate names
    if candidate_name not in candidate_options:
       candidate_options.append(candidate_name) 
    
    #track candidate vote count
       candidate_votes[candidate_name] = 0
    #add a vote to that candidate's count
    candidate_votes[candidate_name] += 1


1.#determine percentage of votes for each candidate
for candidate_name in candidate_votes:
    #retrieve vote count for each
    votes = candidate_votes[candidate_name]
    #calculate percentage of each 
    vote_percentage = float(votes) / float(total_votes) * 100
#print candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage}% of the votes")

#  To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#determine winning vote count and candidate
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)