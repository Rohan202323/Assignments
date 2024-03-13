""" Define a class for the Employee and load all the data as Objects of this class."""
import json

class Employee:
    """This is the Employee class."""
    def __init__(self, emp_data):
        self.emp_id = emp_data['EMP ID']
        self.emp_name = emp_data['EMP NAME']
        self.emp_email = emp_data['EMP EMAIL']
        self.business_unit = emp_data['Business Unit']
        self.salary = emp_data['Salary']

if __name__ == "__main__":
    with open('Employees.json',encoding='utf-8') as file:
        data = json.load(file)


    list_employees = []
    for row in data:
        e = Employee(row)
        #print(row)
        list_employees.append(e)
    #print(list_employees)
