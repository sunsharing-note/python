#! /usr/bin/env python
# -*- coding: utf8 -*-


import socket
import os

sk = socket.socket()

address = ("127.0.0.1",8000)

sk.bind(address)

sk.listen(3)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

while 1:
    conn,addr = sk.accept()
    while 1:
        data = conn.recv(1024)
        cmd,filename,filesize=str(data,"utf8").split("|")
        path = os.path.join(BASE_DIR,"package",filename)
        filesize= int(filesize)

        f = open(path,"ab")
        has_recvd = 0
        while has_recvd != filesize:
            data = conn.recv(1024)
            f.write(data)
            has_recvd += len(data)
        f.close()