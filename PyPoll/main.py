import os
import csv

#specified file to read from
csvpath=os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #read and stored header row
    csvheader = next(csvfile)

    #initialized total votes and created a for loop to add 1 for each row
    #created a listed to store cannidate data
    totalvotes = 0
    candidate = []
    for row in csvreader:
        totalvotes += 1
        candidate.append(row[2])

    #initialized the number of votes for each candidate
    ccsvotes = 0
    dgvotes = 0
    radvotes= 0 

    #created a for loop to using conditional statements to count the number of votes for each candidate
    for i in candidate:
        if i == "Charles Casper Stockham":
            ccsvotes += 1
        elif i == "Diana DeGette":
            dgvotes += 1
        else:
            radvotes += 1

    #calculated each candidate percent votes and rounding to three decimal places       
    ccspercent = round((ccsvotes/totalvotes) * 100, 3) 
    dgpercent = round((dgvotes/totalvotes) * 100, 3)
    radpercent = round((radvotes/totalvotes) * 100, 3)

    #determined the winner by using conditional statements and compared candidate percent votes
    if (ccspercent > dgpercent and ccspercent > radpercent):
        winner = "Charles Casper Stockham"
    elif (dgpercent > ccspercent and dgpercent > radpercent):
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"

    #printed all results
    print("Election Results")
    print("-------------------------")
    print("Total Votes: ", totalvotes)
    print("-------------------------")
    print(f"Charles Casper Stockham: {ccspercent}% ({ccsvotes})")
    print(f"Diana DeGette: {dgpercent}% ({dgvotes})")
    print(f"Raymon Anthony Doane: {radpercent}% ({radvotes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

#specified file to write to
output_path = os.path.join("Analysis", "PyPoll.txt")

#opened file using write mode and wrote results
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {totalvotes}\n")
    file.write("-------------------------\n")
    file.write(f"Charles Casper Stockham: {ccspercent}% ({ccsvotes})\n")
    file.write(f"Diana DeGette: {dgpercent}% ({dgvotes})\n")
    file.write(f"Raymon Anthony Doane: {radpercent}% ({radvotes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
