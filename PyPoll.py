# The data we need to retrieve.
# A complete list of candidates who recieved votes.
# The percentage of votes each Candidate won.
# The total number of votes each candidate won. 
# The winner of the election based on popular vote.

#Resources/election_results.csv
#*import datetime
#*now = datetime.datetime.now()
#*print("The time right now is", now)

#Assigns variable for the file to load and the path
#*file_to_load = 'Resources/election_results.csv'
#Opens the file and reads the file 
#*election_data = open(file_to_load, 'r')
#*print(election_data)

import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file

#Creates filename variable to a dirsct or indirect path to file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#opens the file as a text file
#*with open(file_to_save, "w") as outfile:
#write some data to the file
#*  outfile.write("Counties in the Election\n_______________________\nArapahoe\nDenver\nJefferson")

with open (file_to_load) as election_data:
#Read and analyze data here 
  file_reader = csv.reader(election_data)
  headers = next(file_reader)
  print(headers)

  for row in file_reader:
      print(row)