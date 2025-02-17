import json

from markdown_it.common.html_re import attribute


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
    # Opening JSON file
    f = open('Current_Employees.json')

    # returns JSON object as a list that contains dictionary
    #TODO: I could use table styles from Rich library to present the employee list. NICE TO HAVE
    data = json.load(f)
    for emp in data:
        print(("\n---------------------- " + "\nName: " + emp["first_name"] + " " + emp[
            "last_name"] + "\nDate of Birth: " + str(emp["dob"]) + "\nAge: " + str(emp["age"]) + " Years old" +
               "\nPosition: " + emp["position"] + "\nEmployment Type: " +
               emp["employment_type"] + "\nWork Email: " + emp["work_email"] + "\nSalary: $" + str(float(emp["salary"])) +
               "\nBank Account: " + str(emp["bank_account"]) + "\nDepartment: " + emp["department"] +
               "\nLocation: " + emp["location"]))

def check_duplicates(name, lastName, dob):
    # Opening JSON file
    f = open('Current_Employees.json')
    # returns JSON object as a list that contains dictionary
    data = json.load(f)
    for emp in data:
        while name == emp["first_name"].capitalize() and lastName == emp["last_name"].capitalize() and dob == emp["dob"]:
            print(f"{name.capitalize()} {lastName.capitalize()} with date of birth: {dob} is already registered in the system")
            userChoice = input("Press 1 to enter employee details again, or 2 to cancel this task")

            while userChoice != "1" and userChoice != "2":
                userChoice = input("Please choose between 1 to enter employee details again, or 2 to cancel this "
                                     "task")
            if userChoice == "1":
                name = input("Enter employee's first name").capitalize()
                lastName = input("Enter employee's last name").capitalize()
                dob = input("Enter employee's date of birth (dd/mm/yyyy)")
            elif userChoice == "2":
                #todo: call main manu when is ready
                break

#To check int user inputs (e.g. age and salary)
def check_integer(attribute):
    while not attribute.isnumeric():
        print("Please enter a valid numeric value")
        attribute = input()
    return attribute

def add_employee():
    """To add a new employee to the current list"""
    print("Enter new employee details: ")
    name = input("First name: ").capitalize()
    lastName = input("Lst name: ").capitalize()
    dob = input("Employee's date of birth (dd/mm/yyyy): ")

    #Checkpoint to check duplicates - starts
    check_duplicates(name, lastName, dob)
    # Checkpoint to check duplicates - ends

    #using the function to check the right data type
    age = check_integer(input("Age: "))


    position = input("Position: ").capitalize()
    employment_type = input("Employment type (full-time, part-time, contractor): ").capitalize()
    work_email = input("Work email: ")

    salary = check_integer(input("Salary ($): "))
    bank_account = check_integer(input("Bank account number: "))


    department = input("Department: ").capitalize()
    location = input("Location: ").capitalize()

    # storing values for the new employee in a list of dictionary/ies. Reusing the same as I used for multiple employees
    new_employee = [
        Employee(name, lastName, dob, age, position,
                 employment_type, work_email, salary,
                 bank_account, department, location),
        ]

    # reading and storing existing employees in a temporary list
    with open("Current_Employees.json", "r") as file:
        employees = json.load(file)

    # including this employee to the list (extracting dictionary from new_employee list)
    employees.extend([emp.convert_to_dict() for emp in new_employee])

    # writing all employees (current & new ones) on JSON file
    with open("Current_Employees.json", "w") as file:
        json.dump(employees, file)
    file.close()



    #calling view employees

# ----- Run the program -------
Employee.main()
add_employee()
#todo: user menu
#view_employees()

# writing employees
# To error handling I have to use IOE error script
"""If the file exists, then go and perform the action (r/w/a)
            caseDISPLAY: read the file and display data -> it could be a function to invoke here
            caseAPPEND:
                if name AND lastName already exists
                    "This employee already exists"
                else 
                    append employee
                    display successful message
        else: create the file (w)
        """


def add_employees():
    """To add employees to the current employee list"""
    # Check the file exists and handling if it doesn't
    try:
        # Opening JSON file
        f = open('Current_Employees.json')
        # returns JSON object as a dictionary
        dataDict = json.load(f)
        print(dataDict)
        # Closing file
        f.close()

    except IOError:
        """File doesn't exist so it is created now"""
        f = open("Current_Employees.json", "w")
        # Closing file
        f.close()
