#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:20:41 2020

@author: anjalishaw
"""

import random

black=(0,0,0)
white=(255,255,255)
peach=(255,125,125)
red=(255,0,0)

import pygame
x=pygame.init()

#window
screen_w=700
screen_h=700
game_window=pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("real snakes")
pygame.display.update()

#game specific variables

font=pygame.font.SysFont(None,65)

def show_text(text,color,x,y):
    text_show=font.render(text,True,color)
    game_window.blit(text_show,(x,y))
    
def plot_snake(game_window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_window,black,[x,y,snake_size,snake_size])

#gameloop
def game_loop():
            
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
    
    snake_list=[]
    snake_length=1

    while not exit_game:
        if game_over:
            game_window.fill(white)
            show_text('GAMEOVER! \n Press enter to continue.',peach,0,350)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
            
            if event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_RETURN:   
                    game_loop()
            
        else:
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
                snake_length+=5
                food_x=random.randint(0,screen_w-20)
                food_y=random.randint(0,screen_h-20)
        
                
                
            snake_y+=velocity_y
            snake_x+=velocity_x
          #creating a windowfeature for game      
            game_window.fill(white)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            
            snake_list.append(head)
            '''
             snake_y+=velocity_y
             snake_x+=velocity_x
             
             with the  following code list head and so list snake_list keeps incrementing and so snake length 
             as snake_list is directly used to plot the snake
             so we are using
             if len(snake_list)>snake_length:
                del snake_list[0]
            todelete the unnecessary increment in snake's length'''
          
            if len(snake_list)>snake_length:
                del snake_list[0]
                
            if snake_x<0 or snake_x>screen_w or snake_y<0 or snake_y>screen_h:
                game_over=True
                
            if head in snake_list[:-1]:
                game_over=True
                
            
            pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])
            
            plot_snake(game_window,black,snake_list,snake_size)
           # pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
            show_text("score:" + str(score),peach,5,5)
        clock.tick(fps)
        pygame.display.update()
    
    
    pygame.quit()
    quit()
game_loop()