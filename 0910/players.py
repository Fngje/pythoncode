#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

'''
#列表的切片即使用的列表的一部分元素
players = ['charles','martina','michael','forence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
#倒数三个
print(players[-3:])
'''

#遍历切片
players = ['charles','martina','michael','forence','eli']
print("There is the first three players in my team:")
for palyer in players[:3]:
    print(palyer.title())