#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

motorcycles = ['honda','yamaha','suzuki']

# #修改列表元素
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

#添加列表元素
#1.在列表末尾添加
# motorcycles.append('ducati')
# print(motorcycles)
#2.在指定位置添加
# motorcycles.insert(0,'qianjiang')
# print(motorcycles)
# motorcycles.insert(3,'xihu')
# print(motorcycles)

#删除列表元素
#1.知道要删除的元素的位置可以用del
# del motorcycles[0]
# print(motorcycles)

#3.pop默认删除列表最后一个元素，并可以使这个元素能再次被使用
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print("The last motorcycle I ownd was a " + popped_motorcycles.title() + ".")
# #也可以删除指定位置的元素
# first_ownd = motorcycles.pop(0)
# print("The first motorcycle I ownd was a " + first_ownd.title() + ".")

#3.根据值来删除
motorcycles.remove('yamaha')
print(motorcycles)