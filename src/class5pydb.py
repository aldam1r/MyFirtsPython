# ================================================
# Project:      MyFirstPython
# File:         class5pydb.py
# Author:       Pieter Holthuijsen
# ================================================


from pymysql import *

def connectiontest():
    db = pymysql.connect("192.168.178.101","testuser","Test-123","pydb")
    cursor = db.cursor()
    cursor.execute("select version();")
    data = cursor.fetchone()
    print ("Database version : %s " % data)
    db.close ()

def droptable():
    db = pymysql.connect("192.168.178.101","testuser","Test-123","pydb")
    cursor = db.cursor()
    stmt = """drop table if exists employee"""
    cursor.execute(stmt)
    db.close()

def cretable():
    db = pymysql.connect("192.168.178.101","testuser","Test-123","pydb")
    cursor = db.cursor()
    stmt = """create table employee
              ( first_name      char(30)    not null
              , last_name       char(30)
              , age             integer
              , sex             char(2)
              , income          float
              )"""
    cursor.execute(stmt)
    db.close()


# connectiontest()
# droptable()
# cretable()
