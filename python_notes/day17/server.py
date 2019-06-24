#! /usr/bin/env python
# -*- coding: utf8 -*-


import socket

# 主要有 两个参数: family： AF_INET 服务器之间的通信 AF_UNIX AF_INET6 unix两个不同进程之间的通信
# type:SOCK_STREAM(TCP) SOCK_DGRAM(UDP)
sk = socket.socket()
address = ("127.0.0.1",8000)
sk.bind(address)
sk.listen(3)
conn,addr = sk.accept()
print(conn)
# conn.send("来了 老弟","utf8")
inp = input(">>>>>")
conn.send(bytes(inp,"utf8"))
# conn.close() 关闭这一个链接
# sk.close() 关闭整个server