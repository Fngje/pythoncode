#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

import sys
import pygame

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()