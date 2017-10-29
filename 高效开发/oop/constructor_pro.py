#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang


#构造函数2 通过默认参数实现多种方法构造对象
class MyClass(object):
    message = "Hello,Developer."

    def show(self):
        print(self.message)

    def __init__(self,name = "unset",color = "black"):
        print("Constructor is called with params : ",name," ",color)

inst = MyClass()
inst.show()

inst2 = MyClass("David")
inst2.show()

inst3 = MyClass("Lisa","White")
inst3.show()

inst4 = MyClass(color = "Green")
inst4.show()