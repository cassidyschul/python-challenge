import os
import csv

#specified file to read from
csvpath=os.path.join('Resources', 'budget_data.csv')


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #read and store header row
    csv_header = next(csvfile)

    #initialized total months and created a for loop to add 1 for each row
    total_months = 0
    #initialized net total and created a for loop to add the value in column two for each row
    net_total=0
    #created a list (pybank) to store all data
    pybank = []
    #created a list to store profit/losses data, stored values as integers
    profitlosses=[]

    for row in csvreader:
        total_months += 1
        net_total += int(row[1]) 
        pybank.append(row)
        profitlosses.append(int(row[1]))
   
    #printed results
    print("Finanacial Analysis")
    print("----------------------------")
    
    print("Total Months: ", total_months)

    print(f"Total: ${net_total}")

    #determined first date profit by indexing into pybank the first row second column
    firstdayprofit = int(pybank[0][1])
    #determined last date profit by indexing into pybank the last row second column
    lastdayprofit = int(pybank[-1][1])

    #calculate average change rounding to two decimal places
    average_change= round((lastdayprofit-firstdayprofit)/(total_months-1), 2)

    print("Average Change: $", average_change)
    
    #initialized max and min values
    # maxvalue = 0
    # minvalue = 0

    #initialized difference between profit/losses of the first two cells
    differencesmax = profitlosses[1]-profitlosses[0]
    differencesmin = profitlosses[1]-profitlosses[0]
    
    #started for loop at 1 since already determined the difference of the first two cells
    #initialized first value and second value
    #used conditionals to determine greatest increase and decrease in profit with the associated date
    for i in range(1, total_months-1):
        firstvalue = profitlosses[i]
        nextvalue = profitlosses[i+1]
        if nextvalue - firstvalue > differencesmax:
            differencesmax = nextvalue - firstvalue
            datemax = pybank[i+1][0]
        elif nextvalue - firstvalue < differencesmin:
            differencesmin = nextvalue - firstvalue
            datemin = pybank[i+1][0]    

    #printed results
    print(f"Greatest Increase in Profits: {datemax} (${differencesmax})")
    print(f"Greatest Decrease in Profits: {datemin} (${differencesmin})")

#specified file to write to
output_path = os.path.join("Analysis", "PyBank.txt")

#opened file using write mode and wrote results
with open(output_path, 'w') as file:
    file.write("Finanacial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: {net_total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {datemax} (${differencesmax})\n")
    file.write(f"Greatest Decrease in Profits: {datemin} (${differencesmin})\n")
    



    



    


        
        
    

 