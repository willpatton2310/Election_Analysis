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

#election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:

    #To do: Read and analyze the data
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)
    
    #prints all rows
    # for row in file_reader:
    #     print(row)
        



# #using the with statement open the file as a text file
# with open(file_to_save,"w") as txt_file:
#     #write data to the file
#     txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

