# import modules
import csv
import os

#Source to read budget file
fileload = os.path.join("budget_data.csv")

#file to hold the output of the revenue analysis
outputFile = os.path.join("budgetanalysis.txt")

#variables
totalMonths = 0
totalRevenue = 0 
averagechange = []
months = []

# read csv file
with open(fileload) as budgetData:
    csvreader = csv.reader(budgetData)

    #read header
    header = next(csvreader)
    #move to the first row
    firstRow = next(csvreader)
    
    totalMonths+= 1
    totalRevenue += float(firstRow[1])
    
    #establish the previous revenue
    previousRevenue = float(firstRow[1])

    for row in csvreader:
        totalMonths += 1

        #add the total amount of revenue
        totalRevenue += float(row[1])

        #calculate the net change
        netChange = float(row[1]) - previousRevenue
        #add on to the list of average change
        averagechange.append(netChange)

        #add the first month that a change occured
        months.append(row[0])

        #update the precious renvenue
        previousRevenue = float(row[1])

#calculate the average change per month
averagechangePerMonth = sum(averagechange)/ len(averagechange)

#variables for the greatest increase and decrease
greatestincrease = [months[0], averagechange[0]]
greatestdecrease = [months[0], averagechange[0]]

for m in range(len(averagechange)):
    if(averagechange[m] > greatestincrease[1]):
        greatestincrease[1] = averagechange[m]
        greatestincrease[0] = months[m]
    
    if(averagechange[m] < greatestdecrease[1]):
        greatestdecrease[1] = averagechange[m]
        greatestdecrease[0] = months[m]



#generate ouput 
output = (
    f'Finacial Analysis \n'
    f'-----------------------\n'
    f'Total months = {totalMonths}\n'
    f'Total revenue = ${totalRevenue:,.2f}\n'
    f'Average change = ${averagechangePerMonth:,.2f}\n'
    f'Greatest Increase ={greatestincrease[0]} amount ${greatestincrease[1]:,.2f}\n'
    f'Greatest Decrease ={greatestdecrease[0]} amount ${greatestdecrease[1]:,.2f}'
)
print(output)

#export the output to the output text file
with open(outputFile,"w") as textFile:
    textFile.write(output)