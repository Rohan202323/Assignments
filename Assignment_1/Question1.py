"""
I. Given a String of Characters
1. Print the three most common characters along with their occurrence count.
2. Sort in descending order of occurrence count.
3. If the occurrence count is the same for any character, sort the characters in alphabetical order.
Final Output. 
Top 3 Characters based on the above critera
E.g. 
Input: HAPPIESTMINDS
Output : 
I: 2
P: 2
S: 2
"""
import datetime
import time

def log_function_call(func):
    """Log the function call and execution time"""
    def wrapper(*args, **kwargs):
        #log_file = kwargs.pop("log_file", "execution.txt")
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


def count_character_occurrences(func):
    """Count the character occurrences"""
    def wrapper(*args, **kwargs):
        char_count = {}
        result = func(*args, **kwargs)
        input_str = args[0]
        for char in input_str:
            if char.isalpha():
                char_count[char] = char_count.get(char, 0) + 1
        sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
        for i in range(min(3, len(sorted_chars))):
            print(f"{sorted_chars[i][0]}: {sorted_chars[i][1]}")
        return result

    return wrapper


@log_function_call
@count_character_occurrences
def occurrence_characters(input_str):
    """Count the occurrence of characters in a given sentence"""
    print(input_str)


input_string = input("Enter any string: ")
occurrence_characters(input_string)



# char_count = {}
# def occurence_charcters(input_str):
#     """This function is used to count the occurence of character in given sentence"""
#     for char in input_str:
#         if char.isalpha():
#             char_count[char] = char_count.get(char, 0) + 1
#             #print(char_count[char])
#     return char_count

# input_string =input("enter any string :-  ")
# char_count=occurence_charcters(input_string)
# #print("Character count is :- ",char_count)
# sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
# #print(sorted_chars)
# for i in range(min(3, len(sorted_chars))):
#     print(f"{sorted_chars[i][0]}: {sorted_chars[i][1]}")
