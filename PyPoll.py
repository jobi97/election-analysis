
#add dependencies
import csv
import os
#assign a variable for the file 
'# Add a variable to load a file from a path'
file_to_load = os.path.join("..", "resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("..","analysis", "election_analysis.txt")

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
with open(file_to_load) as election_data:
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
    #save results to text file
with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
    election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    print(total_votes)

#determine percentage of votes for each candidate
    for candidate_name in candidate_votes:
    #retrieve vote count for each
        votes = candidate_votes[candidate_name]
    #calculate percentage of each 
        vote_percentage = float(votes) / float(total_votes) * 100
#print candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Print each candidate's voter count and percentage to the terminal.
    print(candidate_results)
    #  Save the candidate results to our text file.
    xt_file.write(candidate_results)
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
 # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
