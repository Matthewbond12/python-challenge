#Import Dependencies
import os

import csv
#Determine file path and store in new variable for CSV file
with open(os.path.join(r"C:\Users\matth\OneDrive\Desktop\python-challenge\PyPoll\Resources\election_data.csv")) as csvfile:
    election_data = csv.reader(csvfile)

    next(election_data)


#Create and assign variables
   # total_votes = 0
    list_of_candidates = []
  
    number_of_ballots = 0
    first_candidate_votes = 0
    second_candidate_votes = 0
    third_candidate_votes = 0


    #percentage_of_votes = 0
    #most_votes = 0
    # percentage of votes = total votes for candidate / total votes

# Create loop to run through each row and return total votes a
      
    for row in election_data:
        list_of_candidates.append(row[2])
        number_of_ballots += 1

        
       
       
#Generate another list of only unique values in list_of_candidates by modifying list into set 
    unique_list = list(set(list_of_candidates))

    for row in election_data:
        if row[2] == unique_list[0]:
            first_candidate_votes +1

# Print Outputs to Summary Text File

    print(first_candidate_votes)
    print(number_of_ballots)
   
   
    print(unique_list)
    


