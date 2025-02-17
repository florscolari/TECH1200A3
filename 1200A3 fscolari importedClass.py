from Employee import Employee
import json

#Functions

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

