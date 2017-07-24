#================================================
# Project:      MyFirstPython
# File:         solver.py
# Author:       Pieter Holthuijsen
#================================================

import math
from decimal import *


class Solver:
    def calculate(self):
            while True:
                a = int(input("a "))
                b = int(input("b "))
                c = int(input("c "))
                d = b ** 2 - 4 * a * c
                if d > 0:
                    disc = math.sqrt(d)
                    root1 = Decimal(-b + disc) / (2 * a)
                    root2 = Decimal(-b - disc) / (2 * a)
                    r1 = round(root1, 5)
                    r2 = round(root2, 5)
                    print(root1, root2, r1, r2)
                else:
                    print('Error')

Solver().calculate()

