#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#修改前三个外星人的属性
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yelow':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'

#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("......")

#显示创建了多少个外星人
print("Total number of aliens " + str(len(aliens)))