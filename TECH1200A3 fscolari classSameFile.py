import json
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
        return ("\n---------------------- "+ "\nName: " + self.__first_name + " " + self.__last_name + "\nDate of Birth: " + str(self.__dob) + "\nAge: " + str(self.__age) + " Years old" + "\nPosition: " + self.__position + "\nEmployment Type: " +
                self.employment_type + "\nWork Email: " + self.work_email + "\nSalary: $" + str(float(self.__salary)) +
                "\nBank Account: " + str(self.__bank_account) + "\nDepartment: " + self.department +
                 "\nLocation: " + self.location)

    # creating static function main() for creating and using objects from 'Employee' class
    @staticmethod
    def main():
        """initialise the class with 4 employees"""
        emp1 = Employee("Alice", "Anton", "12/12/2002", 23, "Admin",
                        "Full-time", "aanton@company.com", 67000,
                        "66001000123456", "Sales", "Perth")
        emp2 = Employee("Betty", "Bloom", "16/07/1988", 36, "Support Analyst",
                        "Full-time", "bblooom@company.com", 70000,
                        "66001000123434", "Support", "Sydney")
        emp3 = Employee("Caleb", "Connor", "10/02/1987", 38, "Web Developer",
                        "Full-time", "cconnor@company.com",
                        130000, "66001000123423", "IT", "Dunsborough")
        emp4 = Employee("Denton", "Dallas", "04/01/1977", 48, "Infrastructure Consultant",
                        "Part-time", "ddallas@company.com",
                        155000, "66001000127621", "IT", "Perth")
        print(emp1, emp2, emp3, emp4)


# running the application
Employee.main()

#writing employees
#To error handling I have to use IOE error script
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
        emptyList = {""}
        with open('Current_Employees.json', 'w') as file:
            json.dump(emptyList, file)
        file.close()
add_employees()