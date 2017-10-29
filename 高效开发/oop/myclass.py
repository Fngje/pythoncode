#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang


#类和对象
class MyClass(object):
    message = "Hello,Developer."

    def show(self):
        print(self.message)

print(MyClass.message)                  #读取成员变量

MyClass.message = "Good Morning."     #修改成员变量
print(MyClass.message)

inst = MyClass()                        #实例化一个MyClass的对象
inst.message = "Good Evening."        #修改对象的成员变量,不会影响MyClass类的成员变量
inst.show()                             #调用成员参数，无须传入self参数

print(MyClass.message)