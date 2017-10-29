#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang


#构析函数   构造函数的反向函数，在释放（销毁）对象时生效，用来做清理善后工作，释放资源、内存等等
class MyClass(object):
    message = "Hello,Developer."

    def show(self):
        print(self.message)

    def __init__(self,name = "unset",color = "black"):
        print("Constructor is called with params : ",name," ",color)

    def __del__(self):
        print("Desstructor is called.")

inst = MyClass()
inst.show()

inst2 = MyClass("David")
inst2.show()

del inst,inst2

inst3 =MyClass("Lisa","White")
inst3.show()

del inst3