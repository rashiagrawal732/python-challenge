import os
import csv

# Set the directory to the current file directory
os.chdir(os.path.dirname(__file__))

# Path to the CSV file
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Lists to hold profit and date data
profit = []
monthly_changes = []
date = []

# Variables to track totals
count_months = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open and read the CSV file
with open(budget_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)  # Skip the header row

    # Process each row
    for row in csv_reader:
        count_months += 1
        date.append(row[0])
        profit.append(int(row[1]))  # Convert to int

        total_profit += int(row[1])

        # Calculate monthly profit change, skipping the first row
        if count_months > 1:
            monthly_profit_change = int(row[1]) - initial_profit
            monthly_changes.append(monthly_profit_change)

        # Set the initial profit for the next iteration
        initial_profit = int(row[1])

# Calculate average change
average_profit_change = sum(monthly_changes) / len(monthly_changes) if monthly_changes else 0

# Determine greatest increase and decrease in profits
greatest_profit_increase = max(monthly_changes)
greatest_profit_decrease = min(monthly_changes)

# Find corresponding months
profit_month_increase = date[monthly_changes.index(greatest_profit_increase) + 1]  # +1 to adjust for first month
profit_month_decrease = date[monthly_changes.index(greatest_profit_decrease) + 1]

# Print results
print("-----------------------------------------")
print("Financial Analysis")
print("-----------------------------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_profit_change:.2f}")
print(f"Greatest Increase in Profits: {profit_month_increase} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {profit_month_decrease} (${greatest_profit_decrease})")
print("----------------------------------------------------------")

with open('budget_data.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count_months) + "\n")
    text.write("    Total: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_profit_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(profit_month_increase) + " ($" + str(greatest_profit_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(profit_month_decrease) + " ($" + str(greatest_profit_decrease) + ")\n")
    text.write("----------------------------------------------------------\n")
