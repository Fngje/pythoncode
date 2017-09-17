#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

#在函数中修改列表
#首先创建一个列表，期中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_designs = []

#模拟打印每个设计，直到没有未打印的为止
#打印每个设计后，都将其移到列表completed_designs中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_designs.append(current_design)
#显示打印好的所有模型
print("\nThe following models have been printed: ")
print(completed_designs)