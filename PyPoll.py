# #Practicing Pseudocode
#     # 1. Total number of votes cast
#     # 2. A complete list of candidates who received votes
#     # 3. Total number of votes each candidate received
#     # 4. Percentage of votes each candidate won
#     # 5. The winner of the election based on popular vote

# #making connection to the data file Resources/election_results.csv IF it's at the same level then just election_results.csv
# #use / to separate the folders/files

# # Import the datetime class from the datetime module.
# import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()  
# #The first datetime is the datetime module, (first doll). The second datetime is the datetime class (second doll).
# #Then we use datetime attribute now(), (third doll) on the datetime class
# # Print the present time.
# print("The time right now is ", now) #you can use + or , if it's + str(now)

#or to make it less confusing 
# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

#from a import b --> meaning it will only import "class" b from "module" a
#you can write now = datetime.now()  if b is datetime

# import csv #to read a csv file
# #dir is for directory
# print(dir(csv)) #you can use the functions of csv
# print(dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})) 
#dir() will tell functions that goes with the data type; here dictionary
#dir(str) it will give you all the functions that can go with string type

#Open a file 
#file_variable = open(filename, mode)
# file_variable is the name of the variable that will reference the file object.
# filename is a string specifying the name of the file.
# mode is a string specifying the mode for reading or writing the file object. The possible modes are:
# "r": Open a file to be read.
# "w": Open a file to write to it. This will overwrite an existing file and create a file if one does not already exist.
# "x": Open a file for exclusive creation. If the file does not exist, it will not create one.
# "a": Open a file to append data to an existing file. If a file does not exist, it creates one, if a file has been created the data will be added to the file.
# "+": Open a file for reading and writing.

#(Direct Path to the File)
# file = open('Resources/election_results.csv', 'r')
# file.close() #close the file

# with statement without need to close the file
# Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)

# import os #os is module for indirect path "path" is a class and "join" is a function

# file_to_load = 'election_results.csv'
# file2_to_load = 'election_whatver.csv'
# folder_to_load = 'Resources'

# file = os.path.join(folder_to_load, file_to_load)
# file2 = os.path.join(folder_to_load, file2_to_load)
#this way (called chaining) we can make a direct path with appropriate operating system separator
#Above is how Min woul do- set all the variables & below is what the module taught me

# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# #Q: Where can we change the mode of the file?

# #To write to files in Python
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# #this will return an IOError which is an input/output error - meaning we used an output directory that doesn't exist witht the given path
# #But once we make a folder "analysis" in the "Election_Analysis", we will see a text file "election_analysis.txt" in the sidebar


# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the open & close function to write the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World") #write function from the os module

# # Close the file
# outfile.close()

# # Using the with statement open the file as a text file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     # txt_file.write("Hello World")

#     #we can also Write three counties to the file.
#     #  txt_file.write("Arapahoe, ")
#     #  txt_file.write("Denver, ")
#     #  txt_file.write("Jefferson, ")
#     #or  txt_file.write("Arapahoe, Denver, Jefferson")
#     #if we want them in a separate line,use \n
#     #  txt_file.write("Arapahoe\nDenver\nJefferson")

# #Skill Drill
#      txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources/election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # To do: read and analyze the data here.
#    # Read the file object with the reader function.
#     file_reader = csv.reader(election_data) #election_data is the csv file (line 125)
#     # Print each row in the CSV file.
#     # for row in file_reader:
#     #     print(row) #this returned each row as a list
#     #retrieve the first item from each row
#     # for row in file_reader:
#     #     print(row[0])
# # Read and print the header row.
#     headers = next(file_reader)
#     #print(headers)
# #print each row in the CSV file.
#     for row in file_reader:
#         print(row)

# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources/election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # 1. Initialize a total vote counter.
# total_votes = 0

# #4-a. Make a new list where we will put candidate's names
# candidate_options = []

# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # 2. Add to the total vote count.
#         total_votes += 1
#         # 4-b. Print the candidate name from each row
#         candidate_name = row[2]
#         # # 5. Add the candidate name to the candidate list
#         # candidate_options.append(candidate_name)
#         #6. Instead of step 5,
#           # If the candidate does not match any existing candidate...
#         if candidate_name not in candidate_options:
#             # Add it to the list of candidates.
#             candidate_options.append(candidate_name)
# #print the candidate list
# print(candidate_options)
# # # 3. Print the total votes.
# # print(total_votes) #total number of rows without the headers
# # print(f"The total votes are {total_votes:,}")

# #Get the names of candidates by iterating through the rows in the CSV file
# #Then, get the candidates from the “Candidate” column, and then add their names to a list.
# #4. Find the index of Candidate column which is 2 
#     #a) declare a new list, candidate_options = [] by adding it before the with open() statement
#     #b) iterate through the row[2]

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1 
        
        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
          
           # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
# Save the results to our text file.
# Print the candidate vote dictionary.
# print(candidate_votes)
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

# # Determine the percentage of votes for each candidate by looping through the counts.
# # 1. Iterate through the candidate list.
# for candidate in candidate_votes:
#     # 2. Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate]
#     # 3. Calculate the percentage of votes.
#     vote_percentage = int(votes) / int(total_votes) * 100
#     # 4. Print the candidate name and percentage of votes.
#     print(f"{candidate}: received {vote_percentage:.1f}% of the vote.") 

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results= (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    # Save the final vote count to the text file.
        txt_file.write(candidate_results)
   
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)