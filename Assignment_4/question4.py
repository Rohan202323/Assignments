"""Define a method in the class to convert the Employee object to a JSON and write it to a file.
The function should be able to do it for 
* one employee
* List of Employees 
* All(by default)"""
import json

class Employee:
    """This is the Employee"""
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

    def to_dict(self):
        "It return the dictionary.."
        return {
            "EMP ID": self.get_emp_id(),
            "EMP NAME": self.get_emp_name(),
            "EMP EMAIL": self.get_emp_email(),
            "Business Unit": self.get_bu_unit(),
            "Salary": self.get_salary()
        }

    @staticmethod
    def to_json(employees, filename="Employee_all.json"):
        """This is the static method which is used to write in the json file.."""

        if not isinstance(employees, list):
            employees = [employees]

        data = []
        for employee in employees:
            data.append(employee.to_dict())

        with open(filename, "w",encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    
if __name__=="__main__":
    emp1 = Employee("1001", "Mohan raj", "Mohan.raj@example.com", "HR", 70000)
    emp2 = Employee("1002", "Jack Doe", "jack.doe@example.com", "Market", 80000)
    emp3 = Employee("1003", "Shivansh sri", "shivansh.sri@example.com", "Developer", 55000)

    emp1.to_json([emp1], "employee1.json")
    Employee.to_json([emp1, emp2, emp3], "employees_list.json")
    emp_all = [emp1,emp2,emp3]
    Employee.to_json(emp_all)
