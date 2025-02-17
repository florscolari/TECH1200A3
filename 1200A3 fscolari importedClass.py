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

def add_employee():
    """Asking user for values to add an employee"""

    # Reading the current employees from the file and allocating temporary in nested dict
    with open('Current_Employees.json', 'r') as file:
        employee_list = json.load(file)

    print("Enter new employee details:")
    empId = input("Enter an ID")
    name = input("Enter a name")

    # TODO: check for duplicates on the dictionary.

        print("this employee already exist try again")
        name = input("enter another name")
    # I could bring the data as a dictionary: using get? and then use conditionals but HOW?!

    age = int(input("enter age"))
    salary = int(input("enter salary"))
    department = input("Enter a department")
    position = input("Enter a position")
    location = input("Enter a location")

    """formatting user inputs as dictionary"""
    newEmployee = {
        empId:vars(Employee(name,age,salary, department, position, location))}

    #TODO: read more about how I can retrieve data from file and store it in a dictionary
    #Adding the new employee to the list before writing the file
    employee_list.update(newEmployee)

    #Adding the updated list to the file
    write_employees(employee_list)

def view_employees():
    """to read the content on json file"""
    with open('Current_Employees.json', 'r') as file:
        employee_list = json.load(file)
    for emp in employee_list.items():
        print(emp)


#--------- Calling functions to display to the user -----
    #todo: use __str__ to display nicely employees

initial_employees()
add_employee()
view_employees()
