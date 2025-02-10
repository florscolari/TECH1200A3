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

