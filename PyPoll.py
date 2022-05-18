# The data we need to retrieve
#The total number of votes cast
#The complete list of candidates who received votes
#The % of votes won by each candidate
#The total number fo votes each candidate won
#The winner based upon popular vote

#Assign a variable for the file to load and the path
file_to_load = 'Resources\election_results.csv'


# # election_data = open(file_to_load,'r')
# with open(file_to_load) as election_data:

# #To do: perform analysis
#     print(election_data)

#Add our dependencies
import csv
import os

#assign a vaiable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the flie
file_to_save = os.path.join("analysis","election_analysis.txt")

#1. Initialized the total vote counter
total_votes = 0

#create a list of candidate options
candidate_options = []

#Create a candidates dictionary
candidate_votes = {}

#variable for winning candidate
winning_candidate = ""

#variable for winning count
winning_count = 0

#variable for winning percentage
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    
    #prints all rows in the csv file
    for row in file_reader:
        
        #2. Add to the total vote count
        total_votes += 1

        #create candidate name variable and print from each row (third index [0 to 2])
        candidate_name = row[2]

        #Check unique candidate name 
        if candidate_name not in candidate_options:

            #if name is unique, append candidate_options list with the candidates name
            candidate_options.append(candidate_name)

            #Begin tracking the votes for that candidate
            candidate_votes[candidate_name] = 0

        #increment votes for each candidate
        candidate_votes[candidate_name] += 1       

# #print the candidate vote dictionary
# print(candidate_votes)

#Determine the percentage of votes for each candidate by looping through the counts
#1 Interate through the candidate list
for candidate_name in candidate_votes:

    #Initialize votes variable and retrieve the vote count of the candidate
    votes = candidate_votes[candidate_name]

    #Convert votes and total_votes to float point decimal, Initialize voter precentage variable and calculate the vote percentage
    vote_percentage = float(votes) / float(total_votes) * 100

     #Determine the winning vote count and candidate
     #1. Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        
        #if true, set winning_count to votes and winning_percentage to vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage

        #set winning_candidate to the candidate's name
        winning_candidate = candidate_name

    #print the candidate name and vote percentage
    print(f"{candidate_name}: {vote_percentage:.1f}: ({votes:,})\n")
   
#print winning candidate summary
winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------\n")

print(winning_candidate_summary)


    #using the with statement open the file as a text file
    # with open(file_to_save,"w") as txt_file:
        
    # #write results to the file
    # txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

