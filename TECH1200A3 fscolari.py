## Start of the script - 1847863 F. Scolari KBS 2025 TECH1200 Assessment 3

# ----- LIBRARIES / MODULES -----
import json

# ----- CLASS (only 1 class defined on this file) -----
class Employee:
    """To use as a blueprint to have employee objects"""
    __first_name: str
    __last_name: str
    __age: int
    __position: str
    __salary: float
    __dob: str
    __bank_account: str
    department: str
    location: str
    employment_type: str
    work_email: str

    def __init__(self, first_name, last_name, dob, age, position,
                 employment_type, work_email, salary, bank_account, department,
                 location):
        """This is the parameterised constructor to create objects and reference
        variables as object's attributes"""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__age = age
        self.__position = position
        self.employment_type = employment_type
        self.work_email = work_email
        self.__salary = salary
        self.__bank_account = bank_account
        self.department = department
        self.location = location

    # All getters to access and read object's attributes
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_dob(self):
        return self.__dob

    def get_age(self):
        return self.__age

    def get_position(self):
        return self.__position

    def get_employment_type(self):
        return self.employment_type

    def get_work_email(self):
        return self.work_email

    def get_salary(self):
        return self.__salary

    def get_bank_account(self):
        return self.__bank_account

    def get_department(self):
        return self.department

    def get_location(self):
        return self.location

    # All setters to change and update object's attributes
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_dob(self, dob):
        self.__dob = dob

    def set_age(self, age):
        self.__age = age

    def set_position(self, position):
        self.__position = position

    def set_employment_type(self, employment_type):
        self.employment_type = employment_type

    def set_work_email(self, work_email):
        self.work_email = work_email

    def set_salary(self, salary):
        self.__salary = salary

    def set_bank_account(self, bank_account):
        self.__bank_account = bank_account

    def set_department(self, department):
        self.department = department

    def set_location(self, location):
        self.location = location

    def __str__(self):
        return (
                "\n---------------------- " + "\nName: " + self.__first_name + " " + self.__last_name + "\nDate of Birth: " + str(
            self.__dob) + "\nAge: " + str(
            self.__age) + " Years old" + "\nPosition: " + self.__position + "\nEmployment Type: " +
                self.employment_type + "\nWork Email: " + self.work_email + "\nSalary: $" + str(
            float(self.__salary)) +
                "\nBank Account: " + str(self.__bank_account) + "\nDepartment: " + self.department +
                "\nLocation: " + self.location)

    def convert_to_dict(self):
        """To convert an employee class object to a dictionary"""
        return {
            "first_name": self.get_first_name(),
            "last_name": self.get_last_name(),
            "dob": self.get_dob(),
            "age": self.get_age(),
            "position": self.get_position(),
            "employment_type": self.get_employment_type(),
            "work_email": self.get_work_email(),
            "salary": self.get_salary(),
            "bank_account": self.get_bank_account(),
            "department": self.get_department(),
            "location": self.get_location()
        }

    # creating static function main() for creating and using objects from 'Employee' class
    @staticmethod
    def main():
        """initialise the class with 4 employees"""
        employees = [
            Employee("Alice", "Anton", "12/12/2002", 23, "Admin",
                     "Full-time", "aanton@company.com", 67000,
                     "66001000123456", "Sales", "Perth"),
            Employee("Betty", "Bloom", "16/07/1988", 36, "Support Analyst",
                     "Full-time", "bblooom@company.com", 70000,
                     "66001000123434", "Support", "Sydney"),
            Employee("Caleb", "Connor", "10/02/1987", 38, "Web Developer",
                     "Full-time", "cconnor@company.com",
                     130000, "66001000123423", "IT", "Dunsborough"),
            Employee("Denton", "Dallas", "04/01/1977", 48, "Infrastructure Consultant",
                     "Part-time", "ddallas@company.com",
                     155000, "66001000127621", "IT", "Perth")
        ]
        with open('Current_Employees.json', 'w') as file:
            # I cannot use dict methods on a list, but I can use a for loop to use the convert to dict function on each
            # list item
            json.dump([emp.convert_to_dict() for emp in employees], file)
        file.close()


# ----- Functions -----
def view_employees():
    """to display all employees available on JSON & treated as a list of dictionaries"""
    # Opening JSON file
    f = open('Current_Employees.json')

    # returns JSON object as a list that contains dictionaries, 1 for each employee
    data = json.load(f)
    for emp in data:
        print(("\n---------------------- " + "\nName: " + emp["first_name"] + " " + emp[
            "last_name"] + "\nDate of Birth: " + str(emp["dob"]) + "\nAge: " + str(emp["age"]) + " Years old" +
               "\nPosition: " + emp["position"] + "\nEmployment Type: " +
               emp["employment_type"] + "\nWork Email: " + emp["work_email"] + "\nSalary: $" + str(
                    float(emp["salary"])) +
               "\nBank Account: " + str(emp["bank_account"]) + "\nDepartment: " + emp["department"] +
               "\nLocation: " + emp["location"]))

def delete_employee():
    """to delete an employee & get it by its work email as 1 input-only identifier"""
    work_email = input("Work email: ").lower()

    # Opening JSON file
    f = open("Current_Employees.json", "r")

    # returns JSON object as a list that contains dictionaries
    data = json.load(f)

    employee_found = False  # to track if employee already exists -> new tool to me

    for emp in data:
        if emp["work_email"].lower() == work_email:
            employee_found = True
            print(f"Do you want to remove {emp["first_name"]} {emp["last_name"]} ({emp["work_email"]}) from the current employee list? Y/N")
            userConfirmation = input().upper() #Confirmation before deleting employee
            if userConfirmation == "Y":
                data = [emp for emp in data if emp["work_email"] != work_email]
                print(f"{emp["first_name"]} {emp["last_name"]} ({emp["work_email"]}) has been removed from the employee list.")
            elif userConfirmation == "N":
                data = data
            else:
                print("Enter Y or N.")
    if not employee_found:
        print("No employee found.")

    # Save updated list with -1 employee in JSON
    with open("Current_Employees.json", "w") as file:
        json.dump(data, file)
    file.close()

def update_details():
    """to update employee details: get it first by its work email & ask which field wanted to be updated"""
    work_email = input("Work email: ").lower()

    # Opening JSON file
    f = open("Current_Employees.json", "r")

    # returns JSON object as a list that contains dictionary
    data = json.load(f)

    employee_found = False  # to track if employee already exists -> new tool to me

    for emp in data:
        if emp["work_email"].lower() == work_email:
            employee_found = True
            print("What do you want to update?")
            for key in emp.keys():  # displaying all possibles fields for an employee
                key_user = key.lower().replace("_", " ")
                print(f"{key_user}")

            # user's selection
            field_to_update = input("Enter the field name you want to update").lower().replace(" ", "_")
            if field_to_update in emp:
                updated_value = input(f"Enter new value for {field_to_update.lower().replace("_", " ")}: ")
                field_to_update = field_to_update.lower().replace(" ", "_")  # awful in repetition but working
                emp[field_to_update] = updated_value  # updating value
                print(f"{field_to_update.lower().replace("_", " ")} has been updated successfully.")
            else:
                print("Please enter a valid field name.")

    if not employee_found:
        print("No employee found.")

    # Save updated value in JSON
    with open("Current_Employees.json", "w") as file:
        json.dump(data, file)
    file.close()


def view_employee_details():
    """To display all data available for an employee"""
    # set of 3 values to identify an employee uniquely. It is time-consuming (sorry) but working without ID or validation on email.
    first_name = input("First name: ").capitalize()
    last_name = input("Last name: ").capitalize()
    dob = input("Date of birth (dd/mm/yyyy): ")

    # Checkpoint for employee details
    employee_details(first_name, last_name, dob)


def employee_details(first_name, last_name, dob):
    """set of values needed to check for an employee that meets that criteria and display all its data"""
    # Opening JSON file
    f = open('Current_Employees.json')
    # returns JSON object as a list that contains dictionary
    data = json.load(f)

    employees_found = [emp for emp in data if emp["first_name"] == first_name and emp["last_name"] == last_name and
                       emp["dob"] == dob]
    if employees_found:
        for emp in employees_found:
            print(("\n---------------------- " + "\nName: " + emp["first_name"] + " " + emp[
                "last_name"] + "\nDate of Birth: " + str(emp["dob"]) + "\nAge: " + str(emp["age"]) + " Years old" +
                   "\nPosition: " + emp["position"] + "\nEmployment Type: " +
                   emp["employment_type"] + "\nWork Email: " + emp["work_email"] + "\nSalary: $" + str(
                        float(emp["salary"])) +
                   "\nBank Account: " + str(emp["bank_account"]) + "\nDepartment: " + emp["department"] +
                   "\nLocation: " + emp["location"]))
    else:
        print("No employee has been found.")


def search_employee():
    """to search for an employee by: first name, last name or work email"""
    field = input("Enter 1 for first name, 2 for last name or 3 for work email: ").capitalize()
    if field == "1":
        field = "first_name"
        field_user = field_to_field_user(field)
        value = input(f"Enter {field_user}: ").capitalize()
    elif field == "2":
        field = "last_name"
        field_user = field_to_field_user(field)
        value = input(f"Enter {field_user}: ").capitalize()
    elif field == "3":
        field = "work_email"
        field_user = field_to_field_user(field)
        value = input(f"Enter {field_user}: ").lower()  # not happy with adding value within conditional but quick fix to
        # lower and capitalise treatments at this point
    else:
        print("select a valid option: 1, 2 or 3")
    search_employees_by(field, value)

def field_to_field_user(field):
    """to display the field name to the user in a readable-friendly way. e.g no "_" """
    field_user = field.lower().replace("_", " ")
    return field_user

def get_salary(emp):
    """To pass a valid argument for sorting by salary to sort method used to sort the employee list."""
    return emp["salary"]  # the key argument expected on sort() is a function, not a string.
                        # So with this function, I hope to return the value for salary from each dictionary in the list

def get_position(emp):
    """To pass a valid argument for sorting by position to sort method used to sort the employee list."""
    return emp["position"] #same use as salary but now for positions.

def sort_employees():
    """to sort employees by position or by salary, and by A-Z or Z-A"""
    # Opening JSON file
    f = open('Current_Employees.json')

    # returns JSON object as a list that contains dictionary
    data = json.load(f)
    employees_found = []
    f.close()

    for emp in data:
            employees_found.append(emp)

    print("Choose sorting criteria: 1 - Salary or 2 - Position")
    sorting_by_field = input()

    while sorting_by_field != "1" and sorting_by_field != "2":
        print("Please enter a valid choice. 1 for salary or 2 for position")
        sorting_by_field = input()

    print("Choose sorting order: \n A - Ascending (A-Z - Lowest to highest) \n Z - Descending (Z-A - Highest to "
          "lowest )")
    sort_order = input().upper()

    while sort_order != "A" and sort_order != "Z":
        print("Please enter a valid choice. A or Z.")
        sort_order = input().upper()

    if sorting_by_field == "1":
        user_field = "Salary"
        if sort_order == "A":
            user_order = "A-Z"
            employees_found.sort(key=get_salary) #It doesn't accept a string, must be a function
        else:
            user_order = "Z-A"
            employees_found.sort(key=get_salary,reverse=True)

    if sorting_by_field == "2":
        user_field = "Position"
        if sort_order == "A":
            user_order = "A-Z"
            employees_found.sort(key=get_position) #It doesn't accept a string, must be a function
        else:
            user_order = "Z-A"
            employees_found.sort(key=get_position,reverse=True)

    print(f"{len(employees_found)} employees sorted by {user_field} in {user_order} order.")
    for emp in employees_found:
        print(("\n---------------------- " + "\nName: " + emp["first_name"] + " " + emp[
                "last_name"] + "\nDate of Birth: " + str(emp["dob"]) + "\nAge: " + str(emp["age"]) + " Years old" +
                   "\nPosition: " + emp["position"] + "\nEmployment Type: " +
                   emp["employment_type"] + "\nWork Email: " + emp["work_email"] + "\nSalary: $" + str(
                        float(emp["salary"])) +
                   "\nBank Account: " + str(emp["bank_account"]) + "\nDepartment: " + emp["department"] +
                   "\nLocation: " + emp["location"]))

def search_employees_by(field, value):
    """to get & display employees who match field and value"""
    # Opening JSON file
    f = open('Current_Employees.json')

    # returns JSON object as a list that contains dictionary
    data = json.load(f)
    employees_found = []

    field_user = field_to_field_user(field)

    for emp in data:
        if emp[field] == value:
            employees_found.append(emp)
    print(f"We found {len(employees_found)} records with {field_user}: {value}")
    for index, x in enumerate(employees_found, start=1):
        print(index, ".", x["first_name"], x["last_name"], x["dob"], x["position"], x["work_email"], x["location"])

def check_duplicates(first_name, last_name, dob):
    """to get first name, last name and dob from adding an employee & check if a record doesn't exist already in the list"""

    # Opening JSON file
    f = open('Current_Employees.json')

    # returns JSON object as a list that contains dictionary
    data = json.load(f)
    for emp in data:
        if first_name == emp["first_name"].capitalize() and last_name == emp["last_name"].capitalize() and dob == emp[
            "dob"]:
            print(f"{first_name.capitalize()} {last_name.capitalize()} with date of birth: {dob} is already "
                  f"registered in the system")

            while True:
                userChoice = input("Press 1 to enter employee details again, or 2 to cancel this task")

                if userChoice == "1":
                    return "retry"
                elif userChoice == "2":
                    return "cancel"
                else:
                    print("Please enter 1 to enter details again or 2 to cancel this task")



def check_integer(attribute):
    """To check integer data type in user inputs (e.g. age and salary)"""
    while not attribute.isnumeric():
        print("Please enter a valid numeric value")
        attribute = input()
    return int(attribute)


def add_employee():
    """To get the user inputs & append a new employee to the current list"""
    print("-" * 80)
    print("Enter details for the new employee: ")
    while True:
        first_name = input("First name: ").capitalize()
        last_name = input("Last name: ").capitalize()
        dob = input("Date of birth (dd/mm/yyyy): ")

        # Checkpoint to check duplicates - starts
        duplicate_result = check_duplicates(first_name, last_name, dob)  # checking for duplicates. If duplicate is True,
        # it is coming back with a decision to retry or cancel

        ## To handle either is returning duplicate True or False
        if duplicate_result == "cancel":
            print("Task has been cancelled.")
            break
        elif duplicate_result == "retry":
            continue
        # Checkpoint to check duplicates - ends

        # using the function to check the right data type
        age = check_integer(input("Age: "))

        position = input("Position: ").capitalize()
        employment_type = input("Employment type (full-time, part-time, contractor): ").capitalize()
        while employment_type != "Full-time" and employment_type != "Part-time" and employment_type != "Contractor":
            print(f"You wrote: {employment_type}. Please enter: full-time, part-time or contractor")
            employment_type = input().capitalize()

        work_email = input("Work email: ")

        salary = check_integer(input("Salary ($): "))
        bank_account = check_integer(input("Bank account number: "))

        department = input("Department: ").capitalize()
        location = input("Location: ").capitalize()

        # storing values for the new employee in a list of dictionary/ies. Reusing the same as I used for multiple employees
        new_employee = [
            Employee(first_name, last_name, dob, age, position, employment_type, work_email, salary, bank_account,
                     department, location)]

        # reading and storing existing employees in a temporary list
        with open("Current_Employees.json", "r") as file:
            employees = json.load(file)

        # including this employee to the list (extracting dictionary from new_employee list)
        employees.extend([emp.convert_to_dict() for emp in new_employee])

        # writing all employees (current & new ones) on JSON file
        with open("Current_Employees.json", "w") as file:
            json.dump(employees, file)
        file.close()

        # displaying success message
        print("-" * 80)
        print(f"Employee {first_name} {last_name} has been added successfully.")
        break


# Menu options - reusing structure from A2 Ticket Management System
menuOptions = {
    1: "Search for an Employee",
    2: "Add an Employee",
    3: "View Current Employee List",
    4: "View Employee Details",
    5: "Update Employee Details",
    6: "Delete an employee",
    7: "Sort Employees",
    8: "Exit the program"
}


# Welcome & Get the user's name - reusing A2
def welcome(userName):
    """To welcome the user when starting the program"""
    print("-" * 80)
    print("Welcome to Eminent,", userName.title(),
          ".\n" """I am Ema, your Employee Management Assistant. \nLet's sort and organise some people together. What would you like to do next?""")


# Display the main menu
def main_menu():
    """To display the main menu to the user"""
    print("-" * 80)
    for number, task in menuOptions.items():
        print("[", number, "] :", task)
    userMenuChoice = check_integer(input("Choose a number: "))
    while userMenuChoice < 1 or userMenuChoice > 8:  # Checking that is a numeric value within the expected range
        print("Choose a valid number between 1 and 8 please.")
        userMenuChoice = int(input("Choose a number: "))
    return userMenuChoice


# ----- Runinng the program -------

# Initialisation with 4 current employees added to JSON - Current_Employees.json
Employee.main()

print("You are just about to access to the Company's Employee Management System")
userName = input("Enter your name to start: ")
welcome(userName)

while True:
    userChoice = main_menu() # The main menu on a loop to run the program

    if userChoice == 1:
        search_employee()
    elif userChoice == 2:
        add_employee()
    elif userChoice == 3:
        view_employees()
    elif userChoice == 4:
        view_employee_details()
    elif userChoice == 5:
        update_details()
    elif userChoice == 6:
        delete_employee()
    elif userChoice == 7:
        sort_employees()
    elif userChoice == 8:
        print("Exiting Eminent, your Employee Management System. Until next time!")
        break
    else:
        print("Invalid choice. Please try again.")

## End of the script - 1847863 F. Scolari KBS 2025 TECH1200 Assessment 3