"""
2. Using the Dictionary output from assignment 1.b print the output as a Table.
The Headers of a Table are as follows"Name of the Day", "Occurences",
Short Form", "Name in Lower", "Name in upper", "Length"/
"""


import time
import datetime
from tabulate import tabulate

def log_function_call(func):
    """Log the function call and execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        with open("assignment2_execution.txt", "a", encoding="utf-8") as file:
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
            arguments = {"args": args, "kwargs": kwargs}
            file.write(
                f"{func.__module__} {func.__name__} {formatted_time} {arguments}\n"
                f"Function {func.__name__} executed in {end_time - start_time} seconds\n"
            )
        return result

    return wrapper


day_names = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
dict_1 = {}

@log_function_call
def tables():
    """It generates the table in the output"""
    for i, day in enumerate(day_names, start=1):
        dict_1[day] = {
            "Occurrences": i,
            "Short Form": day[:3],
            "Name in lower": day.lower(),
            "Name in upper": day.upper(),
            "Length": len(day)
        }

    headers = ["Name of the Day", "Occurrences", "Short Form",
               "Name in lower", "Name in upper", "Length"]

    table = []
    for day, info in dict_1.items():
        list_1 = [day]
        for header in headers[1:]:
            list_1.append(info[header])
        table.append(list_1)
    print(tabulate(table, headers=headers, tablefmt='grid'))

tables()
# import time
# import datetime
# from tabulate import tabulate


# def log_function_call(func):
#     """Log the function call and execution time"""
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         with open("assignment2_execution.txt", "a", encoding="utf-8") as file:
#             current_time = datetime.datetime.now()
#             formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
#             arguments = {"args": args, "kwargs": kwargs}
#             file.write(
#                 f"{func.__module__} {func.__name__} {formatted_time} {arguments}\n"
#                 f"Function {func.__name__} executed in {end_time - start_time} seconds\n"
#             )
#         return result

#     return wrapper


# day_names= ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# dict_1 = {}

# @log_function_call
# def tables():
#     """It generates the table in the output"""
#     for i, day in enumerate(day_names, start=1):
#         dict_1[day] = {
#             "Occurrences": i,
#             "Short Form": day[:3],
#             "Name in lower": day.lower(),
#             "Name in upper": day.upper(),
#             "Length": len(day)
#         }

#     #print(dict_1)

#     headers = ["Name of the Day", "Occurrences", "Short Form",
#                "Name in lower", "Name in upper", "Length"]


#     table = []
#     for day, info in dict.items():
#         list_1 = [day]
#         #print(list)
#         for header in headers[1:]:
#             list_1.append(info[header])
#             #print(list)
#         table.append(list_1)
#     #print(table)
#     print(tabulate(table, headers=headers,tablefmt='grid'))



# tables()
