#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

age = int(input("Please input your age:"))

if age < 4:
    print("Free!")
elif age < 18:
    print("Cost is $5!")
else:
    print("Cost is $10!")