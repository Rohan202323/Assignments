'''
V.Write a program to print fibonacci series for the given input occurence 
(if user gives i\p as 6 then it should print series till 6th number)
FiBoNACCI series
0 1 1 2 3 5 8 13 21
 
Input: 6, Output: 0 1 1 2 3 5
Input: 10, Output: 0 1 1 2 3 5 8 13 21 34
'''

input = int(input("Enter the number : "))

a = 0
b = 1

if input == 1:
    print(a)
elif input >= 2:
    print(a, b, end=" ")

    for i in range(2, input):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

