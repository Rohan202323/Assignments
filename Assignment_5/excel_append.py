"""pandas is a fast, powerful, flexible and easy to use open source data analysis 
    and manipulation tool,
    built on top of the Python programming language."""
import pandas as pd

# Read the User Excel file
USER_FILE_PATH = 'C:/Users/rohan.rai/Python/User credentials.xlsx'
user_excel = pd.read_excel(USER_FILE_PATH, sheet_name=None)

# Read the Order Excel file
ORDER_FILE_PATH = 'C:/Users/rohan.rai/Python/Order.xlsx'
order_excel = pd.read_excel(ORDER_FILE_PATH)

# Create a new Excel file
OUTPUT_FILE_PATH = 'C:/Users/rohan.rai/Python/saucedemo.xlsx'
with pd.ExcelWriter(OUTPUT_FILE_PATH) as writer:
    # Iterate through each sheet in the User Excel file
    for sheet_name, sheet_data in user_excel.items():
        # Write each sheet to the output Excel file
        print(sheet_name,"----------",sheet_data)
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)
    
    # Append the Order sheet to the output Excel file
    order_excel.to_excel(writer, sheet_name='Order', index=False)

print("Excel sheets appended successfully!")
