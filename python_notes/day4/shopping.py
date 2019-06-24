#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   shopping.py
@Time    :   2018/12/16 14:24:18
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

product_list=[
    ("mac", 9000),
    ("xs max", 8700),
    ("audi", 500000),
    ("water", 1000),
]


shopping_car = []

while True:
    money = input("请输入钱：")
    if money.isdigit():
        money = int(money)
        while True:
            for i, v in enumerate(product_list, 1):
                print(i, v)
            choice = input("请输入编号进行选择[退出:q]；")
            if choice.isdigit():
                choice = int(choice)
                if choice > 0 and choice <= len(product_list):
                    p_item = product_list[choice - 1]
                    if p_item[1] < money:
                        money -= p_item[1]
                        shopping_car.append(p_item)
                    else:
                        print("对不起，您只有%s元钱" % money)
                else:
                    print("编码不存在")    
            elif choice == "q":
                for i in shopping_car:
                    print(i)
                print("您还剩%s元钱"%money)
                break
            else:
                print("输入不合法")
        break
    else:
        print("输入不对")
