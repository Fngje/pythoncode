#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

class MyClass():
    msg = "Hello Developer."

    def show(self):
        print(self.msg)
        print("Here is %s in %s!"%(self.name,self.color))

    def __init__(self,name = "unset",color = "black"):
        print("Constructor is called with params : ",name," ",color)
        self.name = name
        self.color = color

    def __del__(self):
        print("Distructor is called for %s!"%self.name)


inst = MyClass("David")
inst.show()
print("Color of inst is ",inst.color,"\n")

inst2 = MyClass("Lisa","Yellow")
inst2.show()
print("Name of inst2 is %s",inst2.name,"\n")

del inst,inst2