#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang


#构造函数 在对象初始化时生效，为成员变量赋值
class MyClass(object):
    message = "Hello,Developer."

    def show(self):
        print(self.message)

    def __init__(self):
        print("Constructor is called.")     #创建对象时初始化对象，即为对象成员变量赋值

inst = MyClass()                               #初始化对象inst时，inst已经被初始化，并赋值print("Constructor is called.")
inst.show()