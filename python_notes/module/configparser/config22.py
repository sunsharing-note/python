#! /usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

cf = configparser.ConfigParser()

cf.add_section("test")
cf.set("test","count","1")

cf.add_section("test1")
cf.set("test1","name","huahua")

with open("test2.ini","w+") as f:
    cf.write(f)