"""
II. Write a Program 
1. to find all the list of all running process in your System
2. Display the count of each running process.
3. Store this information in a CSV File.
"""

import csv
import wmi

from Logger import Logger



@Logger.log_function_call
def count_process():
    """It will count the process."""
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
        print(f"{process_name}\t{count}")

    CSV_FILE = "counts_process.csv"
    with open(CSV_FILE, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Process Name", "Count"])
        for process_name, count in p_counts.items():
            writer.writerow([process_name, count])
    print(f"Process count has been saved to {CSV_FILE}.")


count_process()




#------------------ previous code -----------------------------------------------------
# import csv
# import wmi

# f = wmi.WMI()

# p_counts = {}

# for process in f.Win32_Process():
#     process_name = process.Name
#     if process_name in p_counts:
#         p_counts[process_name] += 1
#     else:
#         p_counts[process_name] = 1


# print("Process name\tCount")
# for process_name, count in p_counts.items():
#     print(f"{process_name}  {count}")

# CSV_FILE = "counts_process.csv"

# with open(CSV_FILE, mode='w', newline='',encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Process Name", "Count"])
#     for process_name, count in p_counts.items():
#         writer.writerow([process_name, count])

# print(f"Process count has been saved to {CSV_FILE}.")
