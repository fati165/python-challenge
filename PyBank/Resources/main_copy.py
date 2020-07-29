import os
import csv
from pathlib import Path

csvpath= "PyBank.csv"

# two lists: Dates, Profit/Losses
dates = []
revenue = []

# open up the "PyBank.csv" file
with open(csvpath) as csv_file:
    # create a reader object using csv.DictReader
    reader = csv.DictReader(csv_file)
    # loop through each line of our file
    for row in reader:
        # append data within each row to the two lists
        dates.append(row["Date"])
        # convert str to int
        money_str = row["Profit/Losses"]
        money_int = int(money_str)
        revenue.append(money_int)


# total number of months
num_months = len(dates)
# total revenue over span
sum_revenue = sum(revenue)
# average revenue per month
avg_revenue = round(sum_revenue / num_months, ndigits=2)
# max revenue
max_revenue = max(revenue)
max_index = revenue.index(max_revenue)
max_date = dates[max_index]
# min revenue
min_revenue = min(revenue)
min_index = revenue.index(min_revenue)
min_date = dates[min_index]


output = (
    f"Financial Analysis\n" +
    f"----------------------------\n" +
    f"Total Months: {num_months}\n" +
    f"Total: ${sum_revenue}\n" +
    f"Average  Change: ${avg_revenue}\n" +
    f"Greatest Increase in Profits: {max_date} (${max_revenue})\n" +
    f"Greatest Decrease in Profits: {min_date} (${min_revenue})\n"
)

print(output)

with open("../Analysis/output.txt", mode="w") as out_file:
    out_file.write(output)

