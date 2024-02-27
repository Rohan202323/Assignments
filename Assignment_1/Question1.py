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

def OccurenceCharcters(input_string):
    char_count = {}
    for char in input_string:
        if char.isalpha(): 
            char_count[char] = char_count.get(char, 0) + 1 
            #print(char_count[char])
    return char_count

 
input_string =input("enter any string :-  ")
char_count=OccurenceCharcters(input_string)
#print("Character count is :- ",char_count)
sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
#print(sorted_chars)
for i in range(min(3, len(sorted_chars))):
    print(f"{sorted_chars[i][0]}: {sorted_chars[i][1]}")


