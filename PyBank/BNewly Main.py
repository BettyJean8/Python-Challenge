# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    print(first_row)

    # Track the total and net change
    # we have to start at the next row since we already read the first row
    total_months = 1 

    #Starting total net with the first months profit/loss
    total_net = int(first_row [1])

    #Track the first months profit to use for the net change tracking
    previous_net = int(first_row[1])

    #Making a list to store monthly changes for profit and loss
    net_change_list = []

    # Define starting the data list with first row
    data = [first_row]

    # Process each row of data with a for loop 
    for row in reader:
        # Totalling months
        total_months += 1
        # Add profit and loss to the total
        total_net += int(row [1])

        # Track the net change
        current_net = int(row[1])

        # Find the difference from the previous month
        net_change = current_net - previous_net  

        # Store change in our list
        net_change_list.append(net_change)  

        # Update precvious_net to the current profit/loss 
        previous_net = current_net

        # Add current row to the data list
        data.append(row)

        # Will this work?? Let's see...
        #print("Total Months:", total_months)
        #print("Total Net Profit/Loss:", total_net)
        #print("Net Changes:", net_change_list)

    # Calculate the greatest increase in profits (month and amount)
    greatest_increase = max(net_change_list)

    # Using index function to find month that corresponds to max value
    greatest_increase_index = net_change_list.index(greatest_increase)

    # Accounting for starting from second month
    greatest_increase_month = data[greatest_increase_index + 1][0]

    # Does this crazy scheme work?....
    #print("Greatest Increase in Profits:", greatest_increase_month, greatest_increase)


    # Calculate the greatest decrease in profits (month and amount)
    greatest_decrease = min(net_change_list)

    # Using index function to find month that corresponds to max value
    greatest_decrease_index = net_change_list.index(greatest_decrease)
    
    # Accounting for starting from second month
    greatest_decrease_month = data[greatest_decrease_index + 1][0]

    #Did this work?
    #print("Greatest Decrease in Profits:", greatest_decrease_month, greatest_decrease)

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"  # Include the calculated average change
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
