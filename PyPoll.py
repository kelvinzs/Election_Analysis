# The data we need to retrieve.
# A complete list of candidates who recieved votes.
# The percentage of votes each Candidate won.
# The total number of votes each candidate won.
# The winner of the election based on popular vote.

# Resources/election_results.csv
# *import datetime
# *now = datetime.datetime.now()
# *print("The time right now is", now)

# Assigns variable for the file to load and the path
# *file_to_load = 'Resources/election_results.csv'
# Opens the file and reads the file
# *election_data = open(file_to_load, 'r')
# *print(election_data)

import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file

# Creates filename variable to a dirsct or indirect path to file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# opens the file as a text file
# *with open(file_to_save, "w") as outfile:
# write some data to the file
# *  outfile.write("Counties in the Election\n_______________________\nArapahoe\nDenver\nJefferson")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Option
candidate_options = []

# Declare the empty dictionary for candidates
candidate_votes = {}

# winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County Options
county_options = []

# Dictionary for county votes
county_votes = {}

# variables for county with turnout and count
leading_county = ""
county_count = 0

# Open the election result
with open(file_to_load) as election_data:
# Read and analyze election result
  file_reader = csv.reader(election_data)

# Read the header rows
  headers = next(file_reader)
# Print each row in the CSV file
  for row in file_reader:
# Add the total vote count using loop.
      total_votes += 1

      # Print the Candidates name from each row
      candidate_name = row[2]

      # If the candidate does not match any existing candidate
      if candidate_name not in candidate_options:
      # Add the Candidate name to the candidate list
        candidate_options.append(candidate_name)

        # Begin tracking that candidate's vote count
        candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
      candidate_votes[candidate_name] += 1

      # save the result to our text file.
with open(file_to_save, "w") as txt_file:
    # Prints final vote count to terminal
    election_results = (
      f"\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine percentage of votes for each candidate by looping through counts
    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate
      votes = candidate_votes[candidate_name]
      # calculate the percentage of votes
      vote_percentage = float(votes) / float(total_votes) * 100

      # Assigns variable to candidate results
      candidate_results = (
          f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
      # saves candidate result to text file
      txt_file.write(candidate_results)

      # Determine winning vote count and candidate
      # Determine if the votes is greater than winning count
      if (votes > winning_count) and (vote_percentage > winning_percentage):
          # if true set winning count = votes and winning percent = voter_percentage
          winning_count = votes
          winning_percentage = vote_percentage
          # Set the winning_candidate equal to the candidates name
          winning_candidate = candidate_name

          # Prints out each candidate name, vote count, and percentage
          winning_candidate_summary = (
            f"----------------------------\n"
            f"Winner : {winning_candidate}\n"
            f"Winning vote count : {winning_count:,}\n"
            f"Winning percentage: {winning_percentage:.1f}%\n"
            f"-----------------------------\n")

  # Print the total vote
    txt_file.write(winning_candidate_summary)


