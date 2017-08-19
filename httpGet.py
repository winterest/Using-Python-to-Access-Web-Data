# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 22:46:57 2017

@author: lxyxi
"""

import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a socket which is now unconneted
mysock.connect(('data.pr4e.org',80)) # connect the socket with a URL in a certain PORT
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
