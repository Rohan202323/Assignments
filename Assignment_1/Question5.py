'''
V.Write A program to print fibonacci series for the given input occurence 
(if user gives input as 6 then it should print series till 6th number)
FiboNACCI series
0 1 1 2 3 5 8 13 21
 
Input: 6, Output: 0 1 1 2 3 5
Input: 10, Output: 0 1 1 2 3 5 8 13 21 34
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
def fibonacci_sequence(input_num):
    """It generates the fibonacci_series."""
    a = 0
    b = 1

    if input_num == 1:
        return [a]
    elif input_num >= 2:
        sequence = [a, b]

        for _ in range(2, input_num):
            c = a + b
            sequence.append(c)
            a = b
            b = c

        return sequence


input_1 = int(input("Enter the number : "))
fibonacci_seq = fibonacci_sequence(input_1)
print(fibonacci_seq)


# input_1 = int(input("Enter the number : "))

# A = 0
# B = 1

# if input_1 == 1:
#     print(A)
# elif input_1 >= 2:
#     print(A, B, end=" ")

#     for i in range(2, input_1):
#         C = A + B
#         print(C, end=" ")
#         A = B
#         B = C
#End of line(EOl2)
