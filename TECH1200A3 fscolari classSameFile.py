class Employee:
    """To use as a blueprint to have employee objects"""
    __name: str
    __age: int
    __position: str
    __salary: float
    __dob: str
    __bank_account:str
    department: str
    location: str
    employment_type: str
    work_email: str

    def __init__(self, name, age, position, salary, dob, bank_account, department, location, employment_type, work_email):
        """This is the parameterised constructor to create objects and reference
        variables as object's attributes"""
        self.__name = name
        self.__age = age
        self.__position = position
        self.__salary = salary
        self.__dob = dob
        self.__bank_account = bank_account
        self.department = department
        self.location = location
        self.employment_type = employment_type
        self.work_email = work_email

#All getters to access and read object's attributes
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__salary

    def get_dob(self):
        return self.__dob

    def get_bank_account(self):
        return self.__bank_account

    def get_department(self):
        return self.department

    def get_location(self):
        return self.location

    def get_employment_type(self):
        return self.employment_type

    def get_work_email(self):
        return self.work_email

#All setters to change and update object's attributes
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_position(self, position):
        self.__position = position

    def set_salary(self, salary):
        self.__salary = salary

    def set_dob(self, dob):
        self.__dob = dob

    def set_bank_account(self, bank_account):
        self.__bank_account = bank_account

    def set_department(self, department):
        self.department = department

    def set_location(self, location):
        self.location = location

    def set_employment_type(self, employment_type):
        self.employment_type = employment_type

    def set_work_email(self, work_email):
        self.work_email = work_email

    def __str__(self):
        return "Name: " + self.__name + "\tPosition: " + self.__position + "\nYear: " + str(self.__salary)

