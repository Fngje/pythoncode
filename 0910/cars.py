#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

'''
#永久性排序，排序之后列表中元素的顺序无法再次改变
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)#反向排序
print(cars)
'''

'''
#sorted()函数对列表进行临时排序
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:\n %s."%cars)
print("Here is the sorted list:\n %s"%(sorted(cars)))
print("Here is the original list again:\n %s."%cars)
'''

'''
#d倒着打印列表
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:\n %s."%cars)
cars.reverse()
print("Here is the list after the reversal:\n %s."%cars)
'''

#缺点列表吃长度
cars = ['bmw','audi','toyota','subaru']
print(len(cars))