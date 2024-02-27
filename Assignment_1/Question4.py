'''
IV.Write a program to return below output from given input (with and without uses of inbuilt function)
Input -  "My name is Suraj"
output - "Suraj is name My"
'''
def reverse_words(input_str):
    word_list = input_str.split()
    rev_str = ' '.join(word_list[::-1])
    return rev_str

input = input("Enter the String : ")
reversed_string = reverse_words(input)
print(reversed_string)