# this class has three properties for an employee-


class Employees:

    def __init__(self, name, address, grade):
        self.name = name
        self.address = address
        self.grade = grade

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getGrade(self):
        return self.grade
