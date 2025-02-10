from Employee import Employee
import json

#Functions
def initial_employees():
    """To initialise with 4 employee objects"""
    employee_list = { #empty list to store 4 employees
        "emp01": vars(Employee("Adam Sandler", 32, "Web Developer", 120.120, "IT", "Sydney")),
        "emp02": vars(Employee("Betty Bloome", 28, "Support Analyst", 90.230, "Support Desk", "Perth")),
        "emp03": vars(Employee("Caleb Connor", 36, "IT Analyst", 140.570, "IT", "Broome")),
        "emp04": vars(Employee("Donna Tunner", 54, "Admin", 86.000, "Accounting", "Perth"))
    }
    write_employees(employee_list)
    display_json_content()

def write_employees(employeeRecords):
    """to write first 4 employees on a file"""
    with open('Current_Employees.json', 'w') as file:
        json.dump(employeeRecords, file)
    file.close()

#TODO: use a variable for file's name

def display_json_content():
    """to check the content on json file"""
    with open('Current_Employees.json', 'r') as file:
        data = json.load(file)
        print(data)

#todo: function ADD employee
#todo function VIEW all employees

#
#--------- Calling functions to display to the user -----
initial_employees()