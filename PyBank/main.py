import os
import csv
output = "Analysis/"
csvfile=open("Resources/budget_data.csv")
data=csv.reader(csvfile,delimiter=",")
out_file = open(os.path.join(output, "results.txt"), "w")
print("Financial Analysis")
out_file.write("Financial Analysis\n")
print("-"*80 + "\n")
out_file.write("-"*80 + "\n")
dates=[]
numbers=[]
# Looping over the data file-each list were appending Date, Profit/Losses
for row in data:
    dates.append(row[0])
    numbers.append(row[1])
dates=dates[1:]
numbers = list(map(float, numbers[1:]))
TotalMonths=len(dates)
netprofit=sum(numbers)
print("Total Months: {}".format(TotalMonths))
out_file.write("Total Months: {}\n".format(TotalMonths))
print("Total: ${}".format(round(netprofit)))
out_file.write("Total: ${}\n".format(round(netprofit)))
monthlyChanges = []
for i in range(len(numbers)-1):
  changes = numbers[i+1] - numbers[i]
  monthlyChanges.append(changes)
average=sum(monthlyChanges)/len(monthlyChanges)
imin = 0
imax = 0
minimum = monthlyChanges[0]
maximum = monthlyChanges[0]
for i in range(len(monthlyChanges)):
    if monthlyChanges[i] <= minimum:
      imin = i
      minimum = monthlyChanges[i]
    if monthlyChanges[i] >= maximum:
      maximum = monthlyChanges[i]
      imax = i
print("Average Change: ${}".format(round(average, 2)))
out_file.write("Average Change: ${}\n".format(round(average, 2)))
print("Greatest Increase in Profits: {}	(${})".format(dates[imax+1], round(maximum)))
out_file.write("Greatest Increase in Profits: {} (${})\n".format(dates[imax+1], round(maximum)))
print("Greatest Decrease in Profits: {} (${})".format(dates[imin+1], round(minimum)))
out_file.write("Greatest Decrease in Profits: {} (${})".format(dates[imin+1], round(minimum)))

out_file.close()




