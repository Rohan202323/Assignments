# 3. Write the output table from assignment 2 into an Excel File (not CSV).

import pandas as pan
from openpyxl import Workbook
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

a = pan.DataFrame.from_dict(dict, orient='index', columns=["Occurrences", "Short Form", "Name in lower", "Name in upper", "Length"])
a.to_excel("days.xlsx", index_label="Day_Name")