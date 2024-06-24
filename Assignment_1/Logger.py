"""A date in Python is not a data type of its own,
    but we can import a module named datetime to work with dates 
    as date objects.
"""
import datetime
import time


class Logger:
    """decorator"""
    @staticmethod
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

logger = Logger()
