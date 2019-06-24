#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse("xml-test.xml")

root = tree.getroot()

for child in root:
    print(child.tag,child.attrib)
    for child2 in child:
        print(child2.tag,child2.text)

# for node in root.iter("year"):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated","no")
#
# tree.write("xml-test1.xml")

# for country in root.findall("country"):
#     rank = int(country.find("rank").text)
#     if rank >50:
#         root.remove(country)
# tree.write("output.xml")