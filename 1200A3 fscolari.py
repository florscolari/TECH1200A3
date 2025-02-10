from tkinter.font import names

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
    view_employees()

def write_employees(employeeRecords):
    """to write first 4 employees on a file"""
    with open('Current_Employees.json', 'w') as file:
        json.dump(employeeRecords, file)
    file.close()

#TODO: use a variable for file's name
def read_current_employees():
    """to read the current employee list on the file"""
    with open('Current_Employees.json', 'r') as file:
        data = json.load(file)

#todo: function ADD employee
def add_employee():
    """Asking user for values to add an employee"""
    print("Enter new employee details:")
    empId = input("Enter an ID")
    name = input("Enter a name")
    age = int(input("enter age"))
    salary = int(input("enter salary"))
    department = input("Enter a department")
    position = input("Enter a position")
    location = input("Enter a location")
    newEmployee = {
        empId:vars(Employee(name,age,salary, department, position, location))}


    #TODO: check for duplicates on a file (no idea how to do it)

    #Reading the current employees from the file and allocating temporary in nested dict
    with open('Current_Employees.json', 'r') as file:
        employee_list = json.load(file)

    #Adding the new employee to the list before writing the file
    employee_list.update(newEmployee)

    #Adding the updated list to the file
    write_employees(employee_list)

#todo function VIEW all employees
def view_employees():
    """to check the content on json file"""
    with open('Current_Employees.json', 'r') as file:
        employee_list = json.load(file)
    for emp in employee_list.items():
        print(emp)

#--------- Calling functions to display to the user -----
initial_employees()
add_employee()
view_employees()