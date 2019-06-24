#! /usr/bin/env python

line = 1

while line <= 9:
    column = 1
    while column <= line:
        print(str(column) + "*" + str(line) + "=" + str((column * line)), end="\t")
        column += 1
    print()
    line += 1