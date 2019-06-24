#! /usr/bin/env python
# -*- coding: utf8 -*-


import socket
import subprocess


sk = socket.socket()
address = ("127.0.0.1",8000)
sk.bind(address)
sk.listen(3)
conn,addr = sk.accept()
while 1:
    inp = input(">>>>")
    try:
        data = conn.recv(1024)
    except Exception:
        break
    if not data: break
    print("xxxxxx",str(data,"utf8"))
    obj = subprocess.Popen(str(data,"utf8"),shell=True,stdout=subprocess.PIPE)
    cmd_result = obj.stdout.read()
    conn.send(cmd_result)
sk.close()