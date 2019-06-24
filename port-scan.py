#! /usr/bin/python
# -*- coding: utf-8 -*-

import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
remote_server = input("请输入一个IP进行扫描：")
remote_server_ip = socket.gethostbyname(remote_server)
ports = []
print("正在扫描" + remote_server_ip)
socket.setdefaulttimeout(1)
def scan_port(port):

    s = socket.socket(2,1)
    res = s.connect_ex((remote_server_ip,port))
    if res == 0:
        print("Port {}: OPEN".format(port))
    s.close()
for i in range(3300, 3307):
    ports.append(i)
t1 = datetime.now()
pool = ThreadPool(processes = 8)
results = pool.map(scan_port, ports)
pool.close()
pool.join()
print("Multiprocess Scanning Completed in ", datetime.now() - t1)
