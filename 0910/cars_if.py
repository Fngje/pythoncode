#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

'''
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
'''

#条件测试
####检查是否相等
car = 'bmw'
print(car == 'bmw')

car = 'bmw'
print(car == 'audi')

car = 'bmw'
print(car == 'BMW')
#检查是否相等时考虑大小写，如果大小写不一致，返回值为False，当大小写很重要时，这种行为有其优点。
#但当大小写不重要时，只是想检查变量的值，可以将变量转换成小写，再进行比较
car = 'Audi'
print(car.lower() == 'audi')
print(car)