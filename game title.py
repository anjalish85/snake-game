#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:48:39 2020

@author: anjalishaw
"""


import pygame
x=pygame.init()
#window
game_window=pygame.display.set_mode((1200,600))
pygame.display.set_caption("real snakes")
#game specific variables
exit_game=False
game_over=False