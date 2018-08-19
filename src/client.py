# ================================================
# Project:      MyFirstPython
# File:         client.py
# Author:       Pieter Holthuijsen
# ================================================


import socket

# Create object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set host (local machine) and port
host = socket.gethostname()
port = 9999

# Bind to port
clientsocket.connect((host, port))

msg = clientsocket.recv(1024)

clientsocket.close()

print (msg.decode('ascii'))
