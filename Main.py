# this is a main class which instantiates the object from salary class which inherits
# few properties from Employees class


from Salary import *

# main function


def main():
    add_more = "y"
    temp = Salary("Name", "Address", 2)
    Salary.Filecreater(temp)  # creating a temp object to of Salary.filecreator so that it gets me the heading in text file
    while add_more.lower() == 'y':  # a loop to iterate over to take as many as info a user wants
        emp_name = raw_input("Enter your name ")
        emp_address = raw_input("Enter your address")
        emp_grade = input("Enter your grade")
        while emp_grade > 6:
            print "Invalid grade, enter value less than 6"
            emp_grade = input("Enter your grade")
        emp_1 = Salary(emp_name, emp_address, emp_grade) # creating an Employees object
        print emp_1  # printing the info out using __str__ method which is overridden
        Salary.writeInFile(emp_1)  # Calling function from Salary class to write into a file
        add_more = str(raw_input("Do you want to add more customer ? (Y)"))

main()
