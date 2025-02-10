from pydoc import locate


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
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getPosition(self):
        return self.__position

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.department

    def getLocation(self):
        return self.location

#All setters to change and update object's attributes
    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setPosition(self, position):
        self.__position = position

    def setSalary(self, salary):
        self.__salary = salary

    def setDepartment(self, department):
        self.department = department

    def setLocation(self, location):
        self.location = location