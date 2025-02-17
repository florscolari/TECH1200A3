class Employee:
    """To use as a blueprint to have employee objects"""
    __first_name: str
    __last_name: str
    __age: int
    __position: str
    __salary: float
    __dob: str
    __bank_account:str
    department: str
    location: str
    employment_type: str
    work_email: str

    def __init__(self, first_name, last_name, dob, age, position, employment_type, work_email, salary, bank_account, department, location):
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



#All getters to access and read object's attributes
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

#All setters to change and update object's attributes
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
        return "Name: " + self.__first_name + self.__last_name + "\tPosition: " + self.__position + "\nYear: " + str(self.__salary)

  # creating static function main() for creating and using objects from 'Employee' class
    @staticmethod
    def main():
