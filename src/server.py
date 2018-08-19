# ================================================
# Project:      MyFirstPython
# File:         server.py
# Author:       Pieter Holthuijsen
# ================================================


import socket

# Create object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set host (local machine) and port
host = socket.gethostname()
port = 9999

# Bind to port
serversocket.bind((host, port))

# Queue up to 5 requests
serversocket.listen(5)

while True:
    # Establish connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))

    msg='Thank you for connecting' + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()

