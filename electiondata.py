#import modules
import csv
import os

#load in files
inputfile = os.path.join('election_data.csv')

#output the file for analysis
outputfile = os.path.join("electionanalysis.txt")

#variables
totalVotes = 0#total amoiunt of votes
canidates = []# list of canidates
candidatevotes = [] # dictionary to hold the votes each candiate recived
winningcount = 0 # hold winning count
winningcandiate = ""

#read the csv file 
with open(inputfile) as serveyData:
    #creat the csv reader
    csvreader = csv.reader(serveyData)

    #read header
    header = next(csvreader)

    #rows are lists
    #index 0 voter id
    #index 1 county
    #index 2 candiate


    #for each row
    for row in csvreader:
        #add total votes
        totalVotes += 1

        #check to see if candiadte is in list of candidate
        if row [2] not in canidates:
            #if candiadate is not in the list add the candiadte to the list of candiadte
            canidates.append(row[1])

            #add the value to the dictionary
            #value
            candidatevotes[row[2]] = 1

        else:
            # the candiadte is in the list
            #add a vote to the candidate
            candidatevotes[row[2]] += 1

voteoutput = ""

#print(votes)
for candidates in candidatevotes:
    votes = candidatevotes.get(candidates)
    votepct = (float(votes)/float(totalVotes))*100

    voteoutput += f"{candidates}: {votepct:.3f}% \n"

    #compare the winning count
    if votes > winningcount:
        #udate the votes to be the winning count
        winningcount = votes
        #update the winning candiad]te
        winningcandiate = candidates

winngingcandidatesoutput = f"Winner: {winningcandiate}\n"

#set up output
output = (
    f'Election Results\n'
    f'-----------------------\n'
    f'Total Votes:{totalVotes:,}\n'
    f'-----------------------\n'
    f'{voteoutput}\n'
    f'-----------------------\n'
    f'{winngingcandidatesoutput}'
    f"-----------------------"

)


print(output)

#print the results  to text file
with open(outputfile, "w")as textfile:
    textfile.write(output)