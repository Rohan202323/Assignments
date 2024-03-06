"""In this question i logged the information whenever the function is called..."""
import datetime
import json
def log_function_call(func):
    """In this function i created the another function.."""
    def wrapper(*args, **kwargs):
        """This is the wrapper function that logs the function details and 
           calls the wrapped function."""
        current_date = datetime.datetime.now()
        current_datetime = current_date.strftime('%d-%m-%Y %H:%M:%S')
        module_name = func.__module__
        log_file_name = f"{module_name}_{current_date.strftime('%Y%m%d')}.log"
        log_message = f"{module_name} {func.__name__} {current_datetime} {json.dumps(kwargs)}"
        with open(log_file_name, "w", encoding="utf-8") as log_file:
            log_file.write(log_message + "\n")
        with open(log_file_name, "r", encoding="utf-8") as e:
            a = e.read()
            print(a)
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def my_function(arg1, arg2):
    """This is my_function, which prints 'Hello, world!'.
    """
    print("Hello, world!")
    print(arg1,arg2)
my_function(arg1="value1", arg2="value2")

