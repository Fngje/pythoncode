#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

favorite_language = {
    'jen':'python',
    'jack':'english',
    'lily':'chinese',
    'sarah':'ruby'
}

# for name,language in favorite_language.items():
#     print(name.title() + "'s favorite language is " +language.title() + ".")

for name in favorite_language.keys():
    print(name.title())