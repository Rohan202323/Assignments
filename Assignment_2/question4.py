"""
4. Use the python fakr module to generate fak data for the following.
a. Create an excel sheet "Employee Personal Details" with following data.
Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"

	4a. WAF to return the empolyee name with top most salary
	4b. WAF to return the Business Unit with top most aggregated salary
	4c. WAF to return the employee name in each Business Unit with top most salary
	4d. WAF Delete the Record of the Employee name from the Excel File with the least salary.
	4e. WAF to Update the Salary Details of an Employee in the Excel File
"""
#from openpyxl import load_workbook
import time
import datetime
from random import randint
import pandas as pan
from faker import Faker

fak = Faker()

def log_function_call(func):
    """Log the function call and execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        with open("assignment2_execution.txt", "a", encoding="utf-8") as file:
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
            arguments = {"args": args, "kwargs": kwargs}
            file.write(
                f"{func.__module__} {func.__name__} {formatted_time} {arguments}\n"
                f"Function {func.__name__} executed in {end_time - start_time} seconds\n"
            )
        return result

    return wrapper


# a. Create an excel sheet "Employee Personal Details" with following data.
# Generate around 50-100 records
#		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"
employee_data ={}
for i in range(1, 61):
    employee_data[i] = {}
    employee_data[i]['S.No.'] = i
    employee_data[i]['EMP ID'] = randint(1, 61)
    employee_data[i]['EMP NAME'] = fak.name()
    employee_data[i]['EMP EMAIL'] = fak.email()
    employee_data[i]['Business Unit']=fak.random_element(elements=('HR','Finance','IT','Marketing'))
    employee_data[i]['Salary'] = round(randint(40000, 100000), 2)
print(employee_data)



a=pan.DataFrame.from_dict(employee_data,orient='index',columns=["S.No.","EMP ID","EMP NAME","EMP EMAIL","Business Unit","Salary"])
a.to_excel("Employee.xlsx",index=False)

FILE_PATH = 'Employee.xlsx'
# 4a. WAF to return the empolyee name with top most salary
@log_function_call
def employee_name_top_most_salary(path):
    """It returns the empolyee name with top most salary"""
    df = pan.read_excel(path)
    highest_salary = df.loc[df['Salary'].idxmax(), 'EMP NAME']
    return highest_salary

# file_path = 'Employee.xlsx'
highest_salary_employee = employee_name_top_most_salary(FILE_PATH)
print("Employee with the highest salary:", highest_salary_employee)


# 4b. WAF to return the Business Unit with top most aggregated salary

@log_function_call
def bussiness_unit_name(path):
    """It returns the Business Unit with top most aggregated salary"""
    df = pan.read_excel(path)
    grouped_data = df.groupby('Business Unit')['Salary'].sum()
    business_unit_1 = grouped_data.idxmax()

    return business_unit_1


#file_path = 'Employee.xlsx'
aggregated_salary = bussiness_unit_name(FILE_PATH)
print("Business Unit with top most aggregated salary : ", aggregated_salary)


#4c. WAF to return the employee name in each Business Unit with top most salary


@log_function_call
def employee_name_with_high_salary(path):
    """It returns the employee name in each Business Unit with top most salary"""
    df = pan.read_excel(path)
    dictionary = {}

    # Iterate over each unique business unit
    for bus_unit in df['Business Unit'].unique():
        business_unit_df = df[df['Business Unit'] == bus_unit]
        top_salary_employee = business_unit_df.loc[business_unit_df['Salary'].idxmax(), 'EMP NAME']
        dictionary[bus_unit] = top_salary_employee

    return dictionary

#file_path = 'Employee.xlsx'
employee_dict = employee_name_with_high_salary(FILE_PATH)

# Print the employee name in each Business Unit with topmost salary
for business_unit, name in employee_dict.items():
    print(f"Business Unit: {business_unit}, Employee Name: {name}")





# 	4d. WAF Delete the Record of the Employee name from the Excel File with the least salary.
@log_function_call
def delete_employee_least_salary(path):
    """It deletes the Record of the Employee name from the Excel File with the least salary"""
    df = pan.read_excel(path)
    index = df['Salary'].idxmin()
    print("Delete the particular index value :-",index)
    df.drop(index, inplace=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel(path, index=False)


#file_path = 'Employee.xlsx'
delete_employee_least_salary(FILE_PATH)


# 4e. WAF to Update the Salary Details of an Employee in the Excel File
@log_function_call
def update_employee_salary(path, employee_id, new_salary):
    """It updates the Salary Details of an Employee in the Excel File"""

    df = pan.read_excel(path)

    index = df[df['EMP ID'] == employee_id].index
    if len(index) == 0:

        print("Employee not found.")
        return

    df.loc[index, 'Salary'] = new_salary

    df.to_excel(path, index=False)

    print("Employee salary updated successfully.")


#file_path = 'Employee.xlsx'

EMPLOYEE_ID = 50

NEW_SALARY = 50000
update_employee_salary(FILE_PATH, EMPLOYEE_ID, NEW_SALARY)
