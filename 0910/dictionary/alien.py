#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

'''
alien0 = {'color':'green','points':5}
print(alien0['color'])
print(alien0['points'])
alien0['x_position'] = 0
alien0['y_position'] = 25
print(alien0)
'''

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien now is " + alien_0['color'] + ".")

del alien_0['points']
print(alien_0)