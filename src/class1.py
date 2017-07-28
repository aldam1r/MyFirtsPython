# ================================================
# Project:      MyFirstPython
# File:         class1.py
# Author:       Pieter Holthuijsen
# ================================================


class Employee:
    # Common base class.
    empcount = 0

    def __init__(self, p_name, p_salary):
        self.l_name = p_name
        self.l_salary = p_salary
        Employee.empcount += 1

    def __del__(self):
        print(self.l_name + " destroyed!")
        Employee.empcount -= 1

    def display_count(self):
        print("total Employees is %d" % Employee.empcount)

    def display_employee(self):
        print("Name: ", self.l_name, ", Salary: ", self.l_salary)


e1 = Employee("Piet", 3000)
e2 = Employee("Klaas", 2000)
e3 = Employee("Bert", 1000)

try:
    e1.display_count()
    e2.display_count()
    e3.display_count()
    e1.display_employee()
    del e1
    e3.display_count()
    try:
        e1.display_count()  # Error
    except NameError:
        print("Error: Object does not exist.")
    e2.display_count()

except NameError:
    print("Error: Object does not exist.")
