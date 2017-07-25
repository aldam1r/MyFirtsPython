#================================================
# Project:      MyFirstPython
# File:         leeg.py
# Author:       Pieter Holthuijsen
#================================================


def doiets():
    a = str(input("Username: "))
    print(a)
    y = int(a,10)
    print (y)

    i = iter((1,2,3,4))
    for x in i:
        print (x, end=" | ")

doiets()
