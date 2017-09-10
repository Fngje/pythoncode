#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

'''
#自定义元组,用()，而不是[]
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
'''

'''
#元组的内容是不允许修改的，如果要修改元组内容的话，python解释器在运行的时候会报错

#遍历元组中所有的值
for dimension in dimensions:
    print(dimension)
'''

#修改元组变量；虽然元组的元素不能被修改，但可以该存储元组的变量赋值。
dimensions = (200,50)
for dimension in dimensions:
    print(dimensions)

dimensions = (400,100)
for dimension in dimensions:
    print(dimensions)