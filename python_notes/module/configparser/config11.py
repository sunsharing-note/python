#! /usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

cf = configparser.ConfigParser()

cf.read("config.ini")
# 获取section
secs = cf.sections()
print("sections:", secs, type(secs))
# 可选key
opts = cf.options("db")
print(opts)
# 可选key value
kvs = cf.items("db")
print(kvs)

# 获取value
db_host = cf.get("db","db_host")
print(db_host)