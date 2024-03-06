"""Use the python Faker module to generate fake data for the following.
	a. Create an JSON File "Employee Personal Details" with following data. 
        Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"
        """
import json
from faker import Faker

fake = Faker()

employee_details = []

for _ in range(50):  # Generate 50 records
    emp_id = fake.random_int(min=1000, max=9999)
    emp_name = fake.name()
    emp_email = fake.email()
    elements=("Finance", "Marketing", "Sales", "IT", "Operations")
    business_unit = fake.random_element(elements)
    salary = fake.random_int(min=30000, max=100000)

    employee = {
        "EMP ID": emp_id,
        "EMP NAME": emp_name,
        "EMP EMAIL": emp_email,
        "Business Unit": business_unit,
        "Salary": salary
    }
    #print(employee)

    employee_details.append(employee)
    #print("Employee details :-",employee_details)

with open("Employees.json", "w", encoding="utf-8") as json_file:
    json.dump(employee_details, json_file, indent=4)

print("Employee Personal Details file created successfully.")
