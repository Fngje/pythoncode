#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

names = ['jack','tom','bob']
print("People who are %s going to have dinner with me."%names)
print("Unfortunately, %s can not attend."%names[1])
names[1] = 'lily'
print("People who are %s going to have dinner with me."%names)
print("I found a bigger table, so I could invite more people.")
names.insert(0,'erio')
names.insert(2,'lisa')
names.append('leo')
print("People who are %s going to have dinner with me."%names)
print("Just get the message The new table can not be delivered in time, so I can only invite two friends to dinner.")

for i in range(0,4):
    poped_name = names.pop()
    print("I'm so sorry that i can't have dinner with you %s."%poped_name)

print("People who are %s going to have dinner with me."%names)

del names[0]
del names[0]
print("list is that: %s"%names)