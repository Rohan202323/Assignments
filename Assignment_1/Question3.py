'''
(iii) Write a program to monitor the applications running on your system. 
To test: Execute any application like browser, notepad, calculator etc and make sure 
that not more than 2 instances of the same application can be running.
'''

import psutil


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
    #print(f"{app_name} {count}")



