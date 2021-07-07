# The data we need to retrieve
#1. Open the data file.
#2. Write down the names of all the candidates.
#3. Add a vote count for each candidate.
#4. Get the total votes for each candidate.
#5. Get the total votes cast for the election.

#3.4.4 read the election_results csv
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
#1. Declare the empty dictionary.
candidate_votes = {}

#Winning Candidate & Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the Header row
    headers = next(file_reader)
    #Print each row in CSV file
    for row in file_reader:
        #Add to the total vote count.
        total_votes +=1
        #Print the candidate name from each row.
        candidate_name = row[2]
        #Add candidate name to list & track their vote count
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
#Save results to text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"        
            )
    print(election_results, end="")
    #Write some data to the file
    txt_file.write(election_results)
    
    #3.5.4 Determine Candidates' % of Votes
    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        #Calc % of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #create variable to hold election results text
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # print each candidate, vote count, and % to the terminal
        print(candidate_results)
        #save candidate results to text file
        txt_file.write(candidate_results)
    
        #Determine the winning count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes 
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    #Print out winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
        )
    print(winning_candidate_summary)
    
    #Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)