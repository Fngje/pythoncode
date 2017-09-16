#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)