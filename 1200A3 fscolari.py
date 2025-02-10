from Employee import Employee



#Functions

#todo: function write and initialise 4 employee objects
def initial_employees():
    """To initialise with 4 employee objects"""
    employee_list = { #empty list to store 4 employees
        "emp01": vars(Employee("Adam Sandler", 32, "Web Developer", 120.120, "IT", "Sydney")),
        "emp02": vars(Employee("Betty Bloome", 28, "Support Analyst", 90.230, "Support Desk", "Perth")),
        "emp03": vars(Employee("Caleb Connor", 36, "IT Analyst", 140.570, "IT", "Broome")),
        "emp04": vars(Employee("Donna Tunner", 54, "Admin", 86.000, "Accounting", "Perth"))
    }

    print(employee_list.items())
"""
FUNCTION Write_Initial_Employees_To_File()
INITIALIZE employee_list WITH at least 4 Employee objects
OPEN 'Current_Employees' file in write mode
WRITE employee_list to file in chosen format (.txt, .csv, .json)
CLOSE file
"""
"""
"emp02": vars(Employee("Betty Bloome", 28, "Support Analyst", 90.230, "Support Desk", "Perth"))
"emp03": vars(Employee("Caleb Connor", 36, "IT Analyst", 140.570, "IT", "Broome")
"emp04" vars(Employee("Donna Tunner", 54, "Admin", 86.000, "Accounting", "Perth"))
"""
#todo: function ADD employee
#todo function VIEW all employees

#--------- Calling functions to display to the user -----
initial_employees()