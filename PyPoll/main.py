#Import Dependencies
import os

import csv
#Determine file path and store in new variable for CSV file
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
    
with open(csvpath) as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
   

    csv_header = next(election_data)
    print(f"Header': {csv_header}")
#Create and assign variables
    
    list_of_candidates = []
    candidate_votes = {}
    number_of_ballots = 0
    candidate_one_total = 0

    #percentage_of_votes = 0
    #most_votes = 0
    # percentage of votes = total votes for candidate / total votes

# Create loop to run through each row and return total votes a
      
    for row in election_data:
        list_of_candidates.append(row[2])
        number_of_ballots += 1

        
       
       
#Generate another list of only unique values in list_of_candidates by modifying to set
    unique_list = list(set(list_of_candidates))


# Print Outputs to Summary Text File
    for row in election_data:
        candidate_votes{'Candidate': list_of_candidates[2]}


   
   
    print(number_of_ballots)
   
   
    print(unique_list)
    print(unique_list[0])
    







































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































