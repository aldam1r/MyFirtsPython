# ================================================
# Project:      MyFirstPython
# File:         classone.py
# Author:       Pieter Holthuijsen
# ================================================

class Employee:
    # Common base class.
    empcount = 0

    def __init__(self, pName, pSalary):
        self.lName = pName
        self.lSalary = pSalary
        Employee.empcount += 1

    def __del__(self):
        print(self.lName + " destroyed!")
        Employee.empcount -= 1

    def displayCount(self):
        print("total Employees is %d" % Employee.empcount)

    def displayEmployee(self):
        print("Name: ", self.lName, ", Salary: ", self.lSalary)



e1 = Employee("Piet", 3000)
e2 = Employee("Klaas", 2000)
e3 = Employee("Bert", 1000)

try:
    e1.displayCount()
    e2.displayCount()
    e3.displayCount()
    e1.displayEmployee()

    del e1
    e3.displayCount()
    try:
        e1.displayCount() # Error
    except NameError:
        print("Error: Object does not exist.")
     e2.displayCount()

except NameError:
    print("Error: Object does not exist.")


