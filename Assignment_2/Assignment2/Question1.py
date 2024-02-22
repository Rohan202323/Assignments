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

#(a)
a = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
#print(type(a))
grouped_days = list(zip(a, a[1:]))
print(grouped_days)

# dict = { "Monday" : (1,"Monday","Mon","monday","MONDAY",6),
# }


#(b)
def shortForm(data):
    b = data[0:3]
    return b

def lower(data):
    b = data.lower()
    return b
def upper(data):
    b = data.upper()
    return b 


res_dict = {}
for i in range(7):
    dict = {
        a[i] : (i+1,a[i],shortForm(a[i]),lower(a[i]),upper(a[i]),len(a[i]))
       
    }
    res_dict.update(dict)
print(res_dict)


#(c)
occurrences = []

for day in a:
    char_occurrences = {}
    for char in day:
        char_occurrences[char] = day.count(char)
    occurrences.append(char_occurrences)
print(occurrences)
