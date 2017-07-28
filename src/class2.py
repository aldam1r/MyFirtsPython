# ================================================
# Project:      MyFirstPython
# File:         class2.py
# Author:       Pieter Holthuijsen
# ================================================


class Employee:
    "class:     Employee \n\
author:    Pieter"
    empcount = 0

    def __del__(self):
        print(self.l_name + " destroyed!")
        Employee.empcount -= 1

    def set_arg(self, p_name, p_salary):
        self.l_name = p_name
        self.l_salary = p_salary
        Employee.empcount += 1

    def display_count(self):
        print("total Employees is %d" % Employee.empcount)

    def display_employee(self):
        print("Name: ", self.l_name, ", Salary: ", self.l_salary)


e1 = Employee()
e2 = Employee()
e3 = Employee()

# Employee default attibutes
#print("Employee.__bases__: ",  Employee.__bases__)
#print("Employee.__dict__: ",  Employee.__dict__)
#print("Employee.__doc__: ",  Employee.__doc__)
#print(Employee.__doc__)
#print("Employee.__module__: ",  Employee.__module__)
#print("Employee.__name__: ",  Employee.__name__)

e1.set_arg("Piet", 3000)
e2.set_arg("Klaas", 2000)
e3.set_arg("Bert", 1000)

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
