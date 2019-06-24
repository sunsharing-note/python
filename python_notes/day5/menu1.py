#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   munu.py
@Time    :   2018/12/18 20:12:46
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

menu = {
    "北京市": {
        "海淀": {
            "海淀一":{
                "海淀一一":{},
                "海淀一二":{},
            },
            "海淀二":{
                "海淀二一":{},
                "海淀二二":{}, 
            },
        },
        "朝阳": {
            "朝阳一":{
                "朝阳一一":{},
                "朝阳一二":{},
            },
            "朝阳二":{
                "朝阳二一":{},
                "朝阳二二":{},
            },
        },
    },
    "重庆市":{
        "渝北区":{
            "渝北一":{
                "渝北一一":{},
                "渝北一二":{},
            },
            "渝北二":{
                "渝北二一":{},
                "渝北二二":{},
            },

        },
        "江北区":{
            "江北一":{
                "江北一一":{},
                "江北一二":{},
            },
            "江北二":{
                "江北二一":{},
                "江北二二":{},
            },
        },
    },
}

flag = False #默认不回退
quit_flag = False

while not flag and not quit_flag:
    for key in menu:
        print(key)
    choice = input("请输入1：").strip()
    if choice == "q":
        quit_flag = True
    if choice in menu:
        while not flag and not quit_flag:
            for key2 in menu[choice]:
                print(key2)
            choice2 = input("请输入2:").strip()
            if choice2 == "b":
                flag = True
            if choice2 == "q":
                quit_flag = True
            if choice2 in menu[choice]:
                while not flag:
                    for key3 in menu[choice][choice2]:
                        print(key3)
                    choice3 = input("请输入3:").strip()
                    if choice3 == "b":
                        flag = True
                    if choice3 == "q":
                        quit_flag = True
                    if choice3 in menu[choice][choice2]:
                        while not flag and not quit_flag:
                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)
                            print("the ending")    
                            choice4 = input("请输入4:").strip()
                            if choice4 == "b":
                                flag = True
                            if choice4 == "q":
                                quit_flag = True
                        else:
                            flag = False
                else:
                    flag = False
        else:
            flag = False