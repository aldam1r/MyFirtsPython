# ================================================
# Project:      MyFirstPython
# File:         class4.py
# Author:       Pieter Holthuijsen
# ================================================


import re


line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

searchObj = re.search(r'dogs', line, re.M | re.I)
if searchObj:
    print("search --> searchObj.group() : ", searchObj.group())
else:
    print("Nothing found!!")

patt1 = re.compile(r'dogs', re.M | re.I)

matchObj1 = patt1.match(line)
if matchObj1:
    print("match --> matchObj.group() : ", matchObj1.group())
else:
    print("No match!!")

searchObj1 = patt1.search(line)
if searchObj1:
    print("search --> searchObj.group() : ", searchObj1.group())
else:
    print("Nothing found!!")

subobj = patt1.sub('snales', line)
print(subobj)

subobj = patt1.search(line)
print(subobj.group())
print(subobj.groups())