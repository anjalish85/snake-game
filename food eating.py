#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 00:56:10 2020

@author: anjalishaw
"""

import random

black=(0,0,0)
white=(255,255,255)
red=(255,125,125)

import pygame
x=pygame.init()

#window
screen_w=700
screen_h=700
game_window=pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("real snakes")
pygame.display.update()

#game specific variables
exit_game=False
game_over=False
score=0
snake_x=45
snake_y=45

food_x=random.randint(0,screen_w-20)
food_y=random.randint(0,screen_h-20)

velocity_x=0
velocity_y=0
snake_size=10
clock=pygame.time.Clock()
fps=60


#gameloop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                velocity_x+=3
                velocity_y=0
            if event.key ==pygame.K_LEFT:
                velocity_x-=3
                velocity_y=0
            if event.key ==pygame.K_UP:
                velocity_y-=3
                velocity_x=0
            if event.key ==pygame.K_DOWN:
                velocity_y+=3
                velocity_x=0
                
    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=10
        print(score)
        
        food_x=random.randint(0,screen_w-20)
        food_y=random.randint(0,screen_h-20)

        
        
    snake_y+=velocity_y
    snake_x+=velocity_x
  #creating a windowfeature for game      
    game_window.fill(white)
    pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])
    pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
    clock.tick(fps)
    pygame.display.update()


pygame.quit()
quit()