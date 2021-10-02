#The data we need to retrieved
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#Import the datetime class from the datetime module
import datetime as dt

#Use the now() attribute on the dateteime class to get the present time. 
#now =  dt.datetime.now()

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

#Using the with statement open the file as a text file. 
with open(file_to_load) as election_data:

#To Do: Read and analyze the data here. 
    file_reader = csv.reader(election_data)

    #Print each row in the CSV File
    headers = next(file_reader)
    print(headers)




