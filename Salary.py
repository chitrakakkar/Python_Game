# this class inherits the basic properties of an employee and adds salary basis on the grade entered by the user.
# this has a method to simply print the info or write into a file

from Employees import Employees


class Salary(Employees):

         def __init__(self, name, address, grade):
            Employees. __init__(self, name, address, grade)  # Salary class inheriting from Employees

            if self.grade == 1:
                self.salary = 80000

            if self.grade == 2:
                self.salary = 75000

            if self.grade == 3:
                self.salary = 60000

            if self.grade == 4:
                self.salary = 50000

            if self.grade == 5:
                self.salary = 40000

            if self.grade == 6:
                self.salary = 30000


         def __str__(self):    # overidding the method to print what you want
            return "%s who lives at %s falls under %d grade gets salary  = %d  " % (
            self.name, self.address, self.grade, self.salary)

         def getSalary(self):
             return self.salary

         def getName(self):
             return self.name

         def getAddress(self):
             return self.address

         def getGrade(self):
             return self.grade


             # A method to  get the headers for the file
         def Filecreater(self):
             file = open("CustomerInfo1.txt", 'w')
             file.write("Name" + "\t\t\t|Address" + "\t\t\t|Grade" + "\t\t\t|Salary")
             file.close()

         def writeInFile(self):  # a method to write into a file
             file = open("CustomerInfo1.txt", 'a')
             file.write("\n" + str(self.name) )
             file.write("\t\t\t|" + str(self.address))
             file.write("\t\t\t|" + str(self.grade))
             file.write("\t\t\t|" + str(self.salary))
             file.close()

             return
