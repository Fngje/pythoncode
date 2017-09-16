#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

#要求用户输入一个数字，并判断该数字的奇偶，返回给用户
number = int(input("Please enter a number, and I'll tell you if it's evev or odd: "))

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")