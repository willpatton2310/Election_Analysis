# Election_Analysis and Challenge

## Project Overview
A Colorado Board of Elections employee has given us several tasks to complete an election audit of a recent congressional election:

1.  Calculate the total number of votes cast
2.  Get a complete list of candidates who received votes
3.  Calculate the total number of votes each candidate received
4.  Calculate the percentage of votes each candidate won
5.  Determine the winner of the election based on the popular vote

## Resources
- Data Source: eleciton_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.38.1

##Summary
The election analysis shows that:
There were 369,711 total votes in the election
There were three candidates with the following results:
- Diana DeGette won 73.8% of the vote with 272,892 votes and was the winner
- Charles Stockham received 23.0% of the vote with 85,213 votes
- Raymon Doane received 3.1% of the vote with 11,606 votes

##Challenge Summary
Further analysis requested by the client provided a breakdown of the election by county showing:

1. The total number and percentages of votes by county
2. Which county had the largest voter turnout

The results were as follows:
County Votes:
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

Denver county was the largest county with 306,055 votes

##Challenge Overview
This Python script would be usable for any number of candidates and any number of counties to provide the same analysis of an election as long as
the base election data were in the same format and structure.  Candidate or county names could be changed but the output summay would be the same.
