# 3. Write the output table from assignment 2 into an Excel File (not CSV).
"""_summary_"""
import datetime
import time
import pandas as pan




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

day_names= ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
dict_1 = {}


@log_function_call
def table_into_excel():
    """It generates the table in the excel.."""
    for i, day in enumerate(day_names, start=1):
        dict_1[day] = {
            "Occurrences": i,
            "Short Form": day[:3],
            "Name in lower": day.lower(),
            "Name in upper": day.upper(),
            "Length": len(day)
        }

    a = pan.DataFrame.from_dict(dict_1, orient='index',
        columns=["Occurrences", "Short Form", "Name in lower", "Name in upper", "Length"])
    a.to_excel("days.xlsx", index_label="Day_Name")



table_into_excel()
