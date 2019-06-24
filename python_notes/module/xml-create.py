#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

root = ET.Element("home",{"name": "root"})

sub = ET.Element("son",{"sonName": "huahua"})

subsub = ET.Element("subson",{"subsonName":"zhouzhou"})

root.append(sub)
sub.append(subsub)

tree = ET.ElementTree(root)
tree.write("createXml.xml")
