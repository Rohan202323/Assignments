"""
4. Use the python Faker module to generate fake data for the following.
	a. Create an excel sheet "Employee Personal Details" with following data. Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"

	4a. WAF to return the empolyee name with top most salary
	4b. WAF to return the Business Unit with top most aggregated salary
	4c. WAF to return the employee name in each Business Unit with top most salary
	4d. WAF Delete the Record of the Employee name from the Excel File with the least salary.
	4e. WAF to Update the Salary Details of an Employee in the Excel File
"""
from openpyxl import load_workbook
import pandas as pan
from faker import Faker

from random import randint
fake = Faker() 

# a. Create an excel sheet "Employee Personal Details" with following data. Generate around 50-100 records
#		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"
employee_data ={}  
for i in range(1, 61):
    employee_data[i] = {}
    employee_data[i]['S.No.'] = i
    employee_data[i]['EMP ID'] = randint(1, 61)
    employee_data[i]['EMP NAME'] = fake.name()
    employee_data[i]['EMP EMAIL'] = fake.email()
    employee_data[i]['Business Unit'] = fake.random_element(elements=('HR', 'Finance', 'IT', 'Marketing'))
    employee_data[i]['Salary'] = round(randint(40000, 100000), 2)
print(employee_data) 



a = pan.DataFrame.from_dict(employee_data, orient='index', columns=["S.No.","EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
a.to_excel("Employee.xlsx",index=False)


# 4a. WAF to return the empolyee name with top most salary

def employee_name_top_most_salary(file_path):
    df = pan.read_excel(file_path)
    highest_salary = df.loc[df['Salary'].idxmax(), 'EMP NAME']
    return highest_salary

file_path = 'Employee.xlsx'
highest_salary_employee = employee_name_top_most_salary(file_path)
print("Employee with the highest salary:", highest_salary_employee)


# 4b. WAF to return the Business Unit with top most aggregated salary


def bussiness_unit_name(file_path):
    df = pan.read_excel(file_path)
    grouped_data = df.groupby('Business Unit')['Salary'].sum()
    business_unit = grouped_data.idxmax()

    return business_unit


file_path = 'Employee.xlsx'
aggregated_salary = bussiness_unit_name(file_path)
print("Business Unit with top most aggregated salary : ", aggregated_salary)


#4c. WAF to return the employee name in each Business Unit with top most salary



def employee_name_with_high_salary(file_path):
   
    df = pan.read_excel(file_path)
    dictionary = {}

    # Iterate over each unique business unit
    for business_unit in df['Business Unit'].unique():
        business_unit_df = df[df['Business Unit'] == business_unit]
        top_salary_employee = business_unit_df.loc[business_unit_df['Salary'].idxmax(), 'EMP NAME']
        dictionary[business_unit] = top_salary_employee

    return dictionary

file_path = 'Employee.xlsx'
employee_dict = employee_name_with_high_salary(file_path)

# Print the employee name in each Business Unit with topmost salary
for business_unit, name in employee_dict.items():
    print(f"Business Unit: {business_unit}, Employee Name: {name}")





# 	4d. WAF Delete the Record of the Employee name from the Excel File with the least salary.

def delete_employee_least_salary(file_path):
    
    df = pan.read_excel(file_path)
    index = df['Salary'].idxmin()
    print("Delete the particular index value :-",index)
    df.drop(index, inplace=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, index=False)


file_path = 'Employee.xlsx'
delete_employee_least_salary(file_path)


# 4e. WAF to Update the Salary Details of an Employee in the Excel File

def update_employee_salary(file_path, employee_id, new_salary):

    df = pan.read_excel(file_path)

    index = df[df['EMP ID'] == employee_id].index
 
    if len(index) == 0:

        print("Employee not found.")
        
        return

    df.loc[index, 'Salary'] = new_salary

    df.to_excel(file_path, index=False)

    print("Employee salary updated successfully.")
 


file_path = 'Employee.xlsx'

employee_id = 50

new_salary = 50000
 
update_employee_salary(file_path, employee_id, new_salary)






