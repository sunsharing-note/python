#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib


import re

net = re.search("\([^()]+\)", "(1+(2+5*3)*2)")

print(net.group())