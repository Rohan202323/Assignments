"""
2. Using the Dictionary output from assignment 1.b print the output as a Table. The Headers of a Table are as follows
"Name of the Day", "Occurences", Short Form", "Name in Lower", "Name in upper", "Length"/
"""
from tabulate import tabulate
 

day_names= ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
dict = {}

for i, day in enumerate(day_names, start=1):
    dict[day] = {
        "Occurrences": i,
        "Short Form": day[:3],
        "Name in lower": day.lower(),
        "Name in upper": day.upper(),
        "Length": len(day)
    }

#print(dict)

headers = ["Name of the Day", "Occurrences", "Short Form", "Name in lower", "Name in upper", "Length"]


table = []
for day, info in dict.items():
    list = [day]
    #print(list)
    for header in headers[1:]:
        list.append(info[header])
        #print(list)
    table.append(list)
#print(table)
print(tabulate(table, headers=headers,tablefmt='grid'))
