#! /usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

cf = configparser.ConfigParser()

cf.read("test2.ini")
cf.set("test","count","2")
cf.remove_option("test1","name")

with open("test2.ini","w+") as f:
    cf.write(f)