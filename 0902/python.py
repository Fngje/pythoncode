#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang


print("\tpython")
print("Languages:\nPython\nC\nJavaScript")
languages = input("Please input your favorite languages:")
languages = languages.rstrip()
print("Your favorite languages is：" + languages)       #rstrip()方法：去除用户输入中最后的空白
name = input("Please input your name:")
name = name.lstrip()        #lstrip()方法：去除用户输入前面的空白
print(name)