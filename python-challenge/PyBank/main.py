import os
import csv

#Create variables and lists
month_count = 0
total_prof_loss = 0
changes = []
change_months = []
last_month = 0

#Open the file to read
budget_data_csv = os.path.join("Resources/budget_data.csv")
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    header = next(csvreader)

    #go line by line to gather data needed
    for row in csvreader:

        #count the number of months
        month_count += 1

        #calculate total profit
        total_prof_loss =   total_prof_loss + int(row[1])

        #skip the first line for some calculations
        if last_month != 0:

            #check if its an increase or decrease
            if last_month < int(row[1]):
                changes.append(abs(last_month - int(row[1])))
            else:
                changes.append(-abs(last_month - int(row[1])))
            change_months.append(row[0])
        
        #store the profit/loss for next months calculation
        last_month = int(row[1])

#get some final calculations and the months they occured
average_change = round(sum(changes)/len(changes),2)
great_inc = max(changes)
great_inc_month = change_months[changes.index(max(changes))]
great_dec = min(changes)
great_dec_month = change_months[changes.index(min(changes))]

#create a new file to write in
output_file = os.path.join("analysis/budget_data_results.txt")
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("--------------------------\n")
    datafile.write(f"Total Months: {month_count}\n")
    datafile.write(f"Total: ${total_prof_loss}\n")
    datafile.write(f"Average Change: ${average_change}\n")
    datafile.write(f"Greatest Increase in Profits: {great_inc_month} (${great_inc})\n")
    datafile.write(f"Greatest Decrease in Profits: {great_dec_month} (${great_dec})")

#print results to terminal
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_prof_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {great_inc_month} (${great_inc})")
print(f"Greatest Decrease in Profits: {great_dec_month} (${great_dec})\n")