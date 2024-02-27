"""
II. Write a Program 
1. to find all the list of all running process in your System
2. Display the count of each running process.
3. Store this information in a CSV File.
"""


import wmi
import csv

f = wmi.WMI()

p_counts = {}

for process in f.Win32_Process():
    process_name = process.Name
    if process_name in p_counts:
        p_counts[process_name] += 1
    else:
        p_counts[process_name] = 1


print("Process name\tCount") 
for process_name, count in p_counts.items():
    print(f"{process_name}  {count}")

csv_file = "counts_process.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Process Name", "Count"]) 
    for process_name, count in p_counts.items():
        writer.writerow([process_name, count])

print(f"Process count has been saved to {csv_file}.")