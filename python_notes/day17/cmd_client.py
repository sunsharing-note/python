#! /usr/bin/env python
# -*- coding: utf8 -*-


import socket

sk = socket.socket()
address = ("127.0.0.1",8000)

sk.connect(address)

