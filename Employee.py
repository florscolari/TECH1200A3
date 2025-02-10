
class Employee:
    """To use as a blueprint to have employee objects"""
    __name: str
    __age: int
    __position: str
    __salary: float
    department: str
    location: str

#todo: add 4 more attributes

    def __init__(self, name, age, position, salary, department, location):
        """This is the parameterised constructor to create objects and reference
        variables as object's attributes"""
        self.__name = name
        self.__age = age
        self.__position = position
        self.__salary = salary
        self.department = department
        self.location = location

#All getters to access and read object's attributes
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__salary

    def get_department(self):
        return self.department

    def get_location(self):
        return self.location

#All setters to change and update object's attributes
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_position(self, position):
        self.__position = position

    def set_salary(self, salary):
        self.__salary = salary

    def set_department(self, department):
        self.department = department

    def set_location(self, location):
        self.location = location


