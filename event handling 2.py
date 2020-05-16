#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:59:41 2020

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

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                print("you have pressed right key")
                
pygame.quit()
quit()