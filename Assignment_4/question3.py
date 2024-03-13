"""Define getter methods for very attribute of the class.
In this code  define getter .."""
import json

class Employee:
    """This is the Employee class"""
    def __init__(self, emp_id, emp_name, emp_email, bu_unit, salary):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._emp_email = emp_email
        self._bu_unit = bu_unit
        self._salary = salary

    def get_emp_id(self):
        """This is the getter method for EMP ID"""
        return self._emp_id

    def get_emp_name(self):
        """This is the getter method for EMP NAME"""
        return self._emp_name

    def get_emp_email(self):
        """This is the getter method for EMP EMAIL"""
        return self._emp_email

    def get_bu_unit(self):
        """This is the getter method for Business unit"""
        return self._bu_unit

    def get_salary(self):
        """This is the getter method for Salary"""
        return self._salary

if __name__=="__main__":
    with open("Employees.json", "r",encoding='utf-8') as file:
        data = json.load(file)


    lists = []
    for row in data:
        e = Employee(row["EMP ID"], row["EMP NAME"],
                            row["EMP EMAIL"], row["Business Unit"],
                            row["Salary"])
        lists.append(e)


    first_employee = lists[0]
    print("Employee ID:", first_employee.get_emp_id())
    print("Employee Name:", first_employee.get_emp_name())
    print("Employee Email:", first_employee.get_emp_email())
    print("Business Unit:", first_employee.get_bu_unit())
    print("Salary:", first_employee.get_salary())
