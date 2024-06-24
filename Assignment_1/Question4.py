'''
IV.Write a program to return output from given input(with and without uses of inbuilt function)
Input -  "My name is Suraj"
output - "Suraj is name My"
'''

from Logger import Logger


@Logger.log_function_call
def reverse_words(input_str):
    """This function is used to reverse the given word"""
    word_list = input_str.split()
    rev_str = ' '.join(word_list[::-1])
    return rev_str


input_1 = input("Enter the String : ")
REV_STR = reverse_words(input_1)
print(REV_STR)
