# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. Votes for each county
# 7. Percentage of votes each county contributed

import csv
import os
file_to_load = os.path.join("Resources/election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter. 
total_votes = 0
#Make a list of each candidate and dictionary for the total number of votes each received 
candidate_options = []
candidate_votes = {}

#Make a dictionary for the total number of votes each county contributed to the election
county_list = []
county_votes = {}

#Initialize variables for the county that had the largest turnout
largest_county_turnout = ""
winning_county_votes = 0
county_percentage = 0

#Initialize variables for the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open and read the csv file to perform Analysis on
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1 
        
        # Print the candidate name from each row.
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Start the candidate dictionary with the number of votes
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

#Write the results on a text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

#Determine the percentage of votes for each county contributed by looping through the counts
    for county in county_votes:
        votes1 = county_votes[county]
        vote1_percentage = float(votes1)/float(total_votes) * 100
        county_results= (f"{county}: {vote1_percentage:.1f}% ({votes1:,})\n")
        print(county_results)
        txt_file.write(county_results)

#Determine the largest county turn out
        if (votes1 > winning_county_votes) and (vote1_percentage > county_percentage):
            winning_county_votes = votes1
            county_percentage = vote1_percentage
            # And, set the winning_candidate equal to the candidate's name.
            largest_county_turnout = county
    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(largest_county_summary) 
    txt_file.write(largest_county_summary)

#Determine the percentage of votes for each candidate by looping through the counts.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of votes
        candidate_results= (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

#Determine the winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
