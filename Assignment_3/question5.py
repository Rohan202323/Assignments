"""Python has a built-in package called json, 
     which can be used to work with JSON data."""
import json

def aggregated():
    """This function is used to aggregate the Business Unit...."""
    with open("Employees.json", "r", encoding="utf-8") as json_file:
        employee_data = json.load(json_file)
        #print(employee_data)

    aggregated_data = {}
    for employee in employee_data:
        #print("Employee",employee)
        business_unit = employee["Business Unit"]
        #print("bussiness_units::::-",business_unit)
        if business_unit in aggregated_data:
            aggregated_data[business_unit].append(employee)
        else:
            aggregated_data[business_unit] = [employee]
        #print("aggregated_data :--",aggregated_data)

    with open("Aggregated.json", "w", encoding="utf-8") as json_file:
        json.dump(aggregated_data, json_file, indent=4)

    print("Aggregated Employee Details file created successfully.")



def delete_employees(employees_to_delete):
    """function - It deletes the existing employee details"""
    with open("Employees.json", "r", encoding="utf-8") as json_file:
        employee_data = json.load(json_file)

    terminated_employees = []
    for employee in employee_data:
        if str(employee["EMP ID"]) in map(str, employees_to_delete):
            terminated_employees.append(employee["EMP NAME"])
            employee_data.remove(employee)

    if len(terminated_employees) != len(employees_to_delete):
        raise ValueError("One or more employee details not found.")
        #raise Exception("One or more employee details not found.")

    with open("Employees.json", "w", encoding="utf-8") as json_file:
        json.dump(employee_data, json_file, indent=4)

    with open("TerminatedEmployees.json", "w", encoding="utf-8") as json_file:
        json.dump(terminated_employees, json_file, indent=4)

    print("Employee details deleted successfully.")

def salary_hike(hike_percentage):
    """This function is used to hike the salary by 10%"""
    with open("Employees.json", "r", encoding="utf-8") as json_file:
        employee_data = json.load(json_file)
    print("Hii")
    for employee in employee_data:
        #business_unit = employee["Business Unit"]
        original_salary = employee["Salary"]
        hike_amount = original_salary * (hike_percentage / 100)
        new_salary = original_salary + hike_amount
        employee["Salary"] = new_salary

    with open("Employees.json", "w", encoding="utf-8") as json_file:
        json.dump(employee_data, json_file, indent=4)

    print("Salary hike applied successfully.")

# Example usage

# Example usage
aggregated()
employees_to_del = ["1435","5697"]
delete_employees(employees_to_del)

HIKE = 10  # 5% salary hike
salary_hike(HIKE)
