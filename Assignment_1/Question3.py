"""
(iii) Write a program to monitor the applications running on your system. 
To test: Execute any application like browser, notepad, calculator etc and make sure 
that not more than 2 instances of the same application can be running.
"""

import psutil
from Logger import Logger

application_counts = [
    {"process_Name": "chrome.exe", "max_Instances": 2},
    {
        "process_Name": "notepad.exe",
        "max_Instances": 2,
    },
    {"process_Name": "calc.exe", "max_Instances": 2},
    {"process_Name": "msedge.exe", "max_Instances": 2},
    {"process_Name": "firefox.exe", "max_Instances": 2},
]


def count_instances(process):
    """It counts the running instances of the particular application"""

    count = 0
    running_applications = psutil.process_iter(["name"])

    # Iterate through each Process in monitor
    for p in running_applications:
        if p.info["name"] == process:
            count += 1

            # If the no. of running instances exceeds the maximum allowed instances,
            # kill the process
            if count > 2:
                p.kill()
    return count


@Logger.log_function_call
def kill_processes():
    """Kill processes with counts greater than 2"""
    for app in application_counts:
        process_name = app["process_Name"]
        max_instances = app["max_Instances"]

        run_instances = count_instances(process_name)

        if run_instances > max_instances:
            print(
                f"Warning: More than {max_instances} instances of {process_name} running!"
            )
        else:
            print(f"{process_name}: {run_instances}/{max_instances}")


kill_processes()
