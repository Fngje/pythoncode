#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

def print_models(unprinted_designs,completed_designs):
    '''
    #模拟打印每个设计，直到没有未打印的为止
    #打印每个设计后，都将其移到列表completed_designs中
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_designs.append(current_design)

def show_completed_designs(completed_models):
    '''显示打印好的所有模型'''
    print("\nThe following models have been printed: ")
    print(completed_designs)

#创建一个列表，期中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_designs = []

#调用两个函数并传参
print_models(unprinted_designs[:],completed_designs)#利用unprinted_designs[:]创建列表副本，之后的操作只影响副本，原件保持不变
show_completed_designs(completed_designs)
print("\nThe models that i want printing is: " )
print(unprinted_designs)#这里再次打印原件，证实