#! /usr/bin/env python
# -*- coding: utf8 -*-


import socket
import os

sk = socket.socket()

print(sk)
address = ("127.0.0.1",8000)
sk.connect(address)

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

while True:
    inp = input(">>>>>>>").strip()
    cmd,path = inp.split("|")
    #路径拼接尽量用join
    path = os.path.join(BASE_DIR,path)
    filename = os.path.basename(path) # 获得文件名
    file_size = os.stat(path).st_size
    file_info = 'post|%s|%s'%(filename,file_size)
    sk.sendall(bytes(file_info,"utf8"))

    f = open(path,"rb")
    has_sent = 0
    while has_sent != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
    f.close()
    print("success")