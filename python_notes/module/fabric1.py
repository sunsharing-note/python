#! /usr/bin/env python
# -*- coding: utf-8 -*-

import fabric.api

for i in fabric.api.env:
    print(i)

for j in dir(fabric.api):
    print(j)