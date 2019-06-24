#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

def getSelect(Questions):
    select = str(re.findall("(\'.*')",Questions))
    return select[3:-3]

Questions = "show global status like 'Com_select'"
print(getSelect(Questions))
