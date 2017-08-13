# ================================================
# Project:      MyFirstPython
# File:         class5pydb.py
# Author:       Pieter Holthuijsen
# ================================================


import pymysql

db = pymysql.connect("192.168.178.101","testuser","Test-123","pydb")

cursor = db.cursor()

cursor.execute("select version();")

data = cursor.fetchone()

print ("Database version : %s " % data)

db.close
