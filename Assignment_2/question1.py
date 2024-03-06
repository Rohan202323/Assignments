"""1. Create a Tuple with all Days of the week starting from Monday and output the following
	a. A list of tuples which has the two consequtive days grouped together
	b. A dictionary which has the name of the day as the key and value as a tuple with following values
		i. Occurence of the day in a week (e.g. 1 for Monday, 2 for Tuesday)
		ii. Short form of the day (first three letters)
		iii. name of the day in the lower case
		iv. name of the day in the upper case
		v. length of each name

	c. A tuple with all the characters and their number of occurences in each name of the day.
"""


import datetime
import time

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


# (a)
a = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
grouped_days = list(zip(a, a[1:]))
print(grouped_days)


# (b)
@log_function_call
def short_form(data):
    """This function is used to return the first three characters of the string"""
    b = data[0:3]
    return b

@log_function_call
def lower(data):
    """This function is used to convert upper case to lower case"""
    b = data.lower()
    return b

@log_function_call
def upper(data):
    """This function is used to convert lower case to upper case"""
    b = data.upper()
    return b


res_dict = {}
for i in range(7):
    dict_1 = {
        a[i]: (
            i + 1,
            a[i],
            short_form(a[i]),
            lower(a[i]),
            upper(a[i]),
            len(a[i])
        )
    }
    res_dict.update(dict_1)
print(res_dict)


# (c)
@log_function_call
def count_char_occurrences(days):
    """Count the occurrences of each character in a given day"""
    char_occurrences = {}
    for char in days:
        char_occurrences[char] = days.count(char)
    return char_occurrences


occurrences = []
for day in a:
    occurrences.append(count_char_occurrences(day))
print(occurrences)


# #(a)
# a = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
# #print(type(a))
# grouped_days = list(zip(a, a[1:]))
# print(grouped_days)

# # dict = { "Monday" : (1,"Monday","Mon","monday","MONDAY",6),
# # }


# #(b)
# def short_form(data):
#     """This function is used to return first three character of the string"""
#     b = data[0:3]
#     return b

# def lower(data):
#     """This function is used to convert upper case to lower case"""
#     b = data.lower()
#     return b
# def upper(data):
#     """This function is used to convert lower case to upper case"""
#     b = data.upper()
#     return b


# res_dict = {}
# for i in range(7):
#     dict_1 = {
#         a[i] : (i+1,a[i],short_form(a[i]),lower(a[i]),upper(a[i]),len(a[i]))
#     }
#     res_dict.update(dict_1)
# print(res_dict)


# #(c)
# occurrences = []

# for day in a:
#     char_occurrences = {}
#     for char in day:
#         char_occurrences[char] = day.count(char)
#     occurrences.append(char_occurrences)
# print(occurrences)
