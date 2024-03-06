"""
II. Write a Program 
1. to find all the list of all running process in your System
2. Display the count of each running process.
3. Store this information in a CSV File.
"""


import csv
import datetime
import time
import wmi

def log_function_call(func):
    """Log the function call and execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        with open("execution.txt", "a", encoding="utf-8") as file:
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
            arguments = {"args": args, "kwargs": kwargs}
            file.write(
                f"{func.__module__} {func.__name__} {formatted_time} {arguments}\n"
                f"Function {func.__name__} executed in {end_time - start_time} seconds\n"
            )
        return result

    return wrapper


@log_function_call
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
