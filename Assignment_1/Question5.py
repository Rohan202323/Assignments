'''
V.Write A program to print fibonacci series for the given input occurence 
(if user gives input as 6 then it should print series till 6th number)
FiboNACCI series
0 1 1 2 3 5 8 13 21
 
Input: 6, Output: 0 1 1 2 3 5
Input: 10, Output: 0 1 1 2 3 5 8 13 21 34
'''


from Logger import Logger


@Logger.log_function_call
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
