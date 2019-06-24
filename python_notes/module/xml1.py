#! /usr/bin/env python
# -*- coding: utf-8 -*-

import  xml.etree.ElementTree as ET


with open("xml-test.xml","r") as file:
    strXML = file.read()
    root = ET.XML(strXML)
 #   print(root.tag)

# tree = ET.parse("xml-test.xml")
#
# root = tree.getroot()
# for value in root.iter("year"):
#     print(value.tag,value.text)

    node = root.find("name")
    print(node)

# for child in root:
#     print(child.tag,child.attrib)
#     for child2 in child:
#         print(child2.tag,child2.text)
#print(root.tag)

# for node in root.iter("year"):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated","xxx")
# tree.write("xml-test.xml")