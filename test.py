#! /usr/bin/env python

import re

def tt(str):
    ret = re.findall("\w{1,20}/(\w{1,20}[-_]?\w{1,20}[-_]?\w{1,20}/?\w{1,5})",str)
    return ret[0]

# ss = tt("sc/cmccsq-v2-device")
# print(ss)
