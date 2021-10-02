#The data we need to retrieved
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Declare New list for candidate names
candidate_options = []

#Decare Empty dictionary
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = 0
winning_count = 0
winning_percentage = 0



#Using the with statement open the file as a text file. 
with open(file_to_load) as election_data:

#To Do: Read and analyze the data here. 
    file_reader = csv.reader(election_data)

    #Print each row in the CSV File
    headers = next(file_reader)
    for row in file_reader:
        #Add to the total vote count
        total_votes+=1

        #Print the candidate name from each row
        candidate_name= row[2]

        #IF the candidate name does not match existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #begin tracking that candidate's vote count.
            candidate_votes[candidate_name]= 0

        #counting votes for candidates
        candidate_votes[candidate_name]+=1

#save the results to our text file
with open(file_to_save,"w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"
    f"------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"------------------------\n")

    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)
    
    
    #Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        
        #retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        #calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes)*100

        candidate_results = (f" {candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        


        print(candidate_results)
        txt_file.write(candidate_results)


        #determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

        #if true then set the winning_count = votes and winning_percent = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage

            #set the winning candidate equal to the candidates name
            winning_candidate = candidate_name
            
            #to Do: print out the winning candidate, vote and percentage to terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")
        
    
    winning_candidate_summary = (   
        f"------------------\n"
        f"Winner: {winning_candidate}\n"   
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------\n")
    
    print(winning_candidate_summary)
    #save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)



    

    
    

