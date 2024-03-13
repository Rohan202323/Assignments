"""Define setter methods for every attribute of the class.
   a. Set the value passed to it as a parameter
    b. Use Faker module to set the value as default"""

import json
from faker import Faker

fake = Faker()

class Employee:
    """This is the Employee class"""
    def __init__(self, emp_id=None, emp_name=None, emp_email=None, business_unit=None, salary=None):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._emp_email = emp_email
        self._business_unit = business_unit
        self._salary = salary

    @property
    def emp_id(self):
        """Property of emp_id"""
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value

    @property
    def emp_name(self):
        """Property of emp_name"""
        return self._emp_name

    @emp_name.setter
    def emp_name(self, value):
        self._emp_name = value

    @property
    def emp_email(self):
        """Property of emp_email"""
        return self._emp_email

    @emp_email.setter
    def emp_email(self, value):
        self._emp_email = value

    @property
    def business_unit(self):
        """Property of business_unit"""
        return self._business_unit

    @business_unit.setter
    def business_unit(self, value):
        self._business_unit = value

    @property
    def salary(self):
        """Property of salary.."""
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

if __name__ == "__main__":
    with open('Employees.json',encoding='utf-8') as file:
        data = json.load(file)

    lists = []
    for row in data:
        e = Employee(
            emp_id=row.get('EMP ID', fake.random_number(digits=4)),
            emp_name=row.get('EMP NAME', fake.name()),
            emp_email=row.get('EMP EMAIL', fake.email()),
            business_unit=row.get('Business Unit', fake.job()),
            salary=row.get('Salary', fake.random_number(digits=5))
        )
        lists.append(e)
    #print(lists)
