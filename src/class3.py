 # ================================================
# Project:      MyFirstPython
# File:         class3.py
# Author:       Pieter Holthuijsen
# ================================================


class Vector:
    'Class for testing overloading operators'
    def __init__(self, p_c1, p_c2):
        self.l_c1 = p_c1
        self.l_c2 = p_c2

    def __str__(self):
        return 'Vector (%d, %d)' % (self.l_c1, self.l_c2)

    def __sub__(self, other):
        return Vector(self.l_c1 - other.l_c1, self.l_c2 - other.l_c2)

p_c1, p_c2 = 2, 2
v1 = Vector(p_c1,p_c2)
v2 = Vector(1,1)
v3 = Vector(1,1)
print(v1 - v2)
print(v1.l_c1 + v2.l_c2)
print(v1 - v2 - v3 - v1)
