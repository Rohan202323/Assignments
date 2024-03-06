'''
IV.Write a program to return output from given input(with and without uses of inbuilt function)
Input -  "My name is Suraj"
output - "Suraj is name My"
'''



import datetime
import time


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
def reverse_words(input_str):
    """This function is used to reverse the given word"""
    word_list = input_str.split()
    rev_str = ' '.join(word_list[::-1])
    return rev_str


input_1 = input("Enter the String : ")
REV_STR = reverse_words(input_1)
print(REV_STR)



# def reverse_words(input_str):
#     """This function is used to reverse the given word"""
#     word_list = input_str.split()
#     rev_str = ' '.join(word_list[::-1])
#     return rev_str

# input_1 = input("Enter the String : ")
# REV_STR = reverse_words(input_1)
# print(REV_STR)
