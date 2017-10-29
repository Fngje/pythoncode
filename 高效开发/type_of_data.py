#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

import math

num1 = input("Pls enter a number: ")
num2 = input("Pls enter a number: ")
if num1 > num2:
    print("%s > %s"%(num1,num2))
elif num1 == num2:
    print("%s = %s"%(num1,num2))
else:
    print("%s < %s"%(num1,num2))

# a = cmp(num1,num2)    python3中没有cmp函数了，在python2中才可以使用
# print(a)