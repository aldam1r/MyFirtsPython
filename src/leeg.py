# ================================================
# Project:      MyFirstPython
# File:         leeg.py
# Author:       Pieter Holthuijsen
# ================================================
# import sys
import calendar

import time

import printer

gPar = "Global 1"

def doiets():
    a = str(input("Username: "))
    print(a)
    y = int(a, 10)
    print(y)


def doiter():
    i = iter((1, 2, 3, 4))
    for x in i:
        print(x, end=" | ")

    print ("\n")


def dofibonacci(z=''):
    def fibonacci(n):
        a = 0
        b = 1
        c = 0
        while True:
            if(c > n): return
            yield a
            a, b = b, a + b
            c += 1
    if(z == ''): z = 5
    f = fibonacci(z)
    for x in f:
        print(x, end=" ^ ")
    print ("\n")
    f = fibonacci(z)
    for y in f:
        d = 2
        e = (y>d)-(y<d)
        print(e, end=" % ")


def doarray():
    d = {}
    k = (1,2,3,4)
    for a in k:
        d[a] = ('a'*a)
    if (d[3] == 'aaa'):
        print(d[4])

def docalendar():
    c = calendar.month(2017, 4)
    print("pick a date:")
    print(c)


def dotime1():
    a = str(time.time())
    print("Time: "+a)


def dotime2():
    a = time.strftime('%H:%M',time.localtime())
    print("Time: "+a)


def doreturn():
    lPar = "Local 1"
    global gPar
    gPar = lPar
    print("Global in function: "+gPar)
    return gPar

def docontent():
    content=dir(time)
    print(content)


# doiets()
# doiter()
# dofibonacci()
# dofibonacci(9)
# dofibonacci(z=9)
# doarray()
# docalendar()
# dotime1()
# dotime2()
# print("Global in main: " + gPar)
# doreturn()
# print("Global in main: " + gPar)
# print("\n")
# gPar = doreturn() # Not manditory. Function can replace or set a global when global is referenced.
# print("Global in main: " + gPar)
# docontent()
printer.inktjet.Inktjet()
printer.Laser()
printer.Matrix()