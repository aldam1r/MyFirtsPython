# ================================================
# Project:      MyFirstPython
# File:         email.py
# Author:       Pieter Holthuijsen
# ================================================

import smtplib

sender = 'ikke@tamtam.nl'
receivers = ['self@tamtam.nl']

message = """ From: From ikke <bla>
To: To self <bla>
Subject: testing

This is a test
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print "Succes"
except SMTPException:
    print "Error sending email"