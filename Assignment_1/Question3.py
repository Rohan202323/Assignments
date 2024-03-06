'''
(iii) Write a program to monitor the applications running on your system. 
To test: Execute any application like browser, notepad, calculator etc and make sure 
that not more than 2 instances of the same application can be running.
'''


import datetime
import time
import psutil


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
def processes():
    """process"""
    application_counts = {}
    for process in psutil.process_iter(['name']):
        app_name = process.info['name']
        if app_name in application_counts:
            application_counts[app_name] += 1
        else:
            application_counts[app_name] = 1
    for app_name, count in application_counts.items():
        if count > 2:
            print(f"Warning: More than 2 instances of {app_name} running!")

processes()








# import psutil


# application_counts = {}
# for process in psutil.process_iter(['name']):
#     app_name = process.info['name']
#     if app_name in application_counts:
#         application_counts[app_name] += 1
#     else:
#         application_counts[app_name] = 1
# for app_name, count in application_counts.items():
#     if count > 2:
#         print(f"Warning: More than 2 instances of {app_name} running!")
#     #print(f"{app_name} {count}")
