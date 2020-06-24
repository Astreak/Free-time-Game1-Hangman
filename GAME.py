import pygame
import numpy as np
import os
import sys
from pygame.locals import *
#initialize
pygame.init()
#form the window
win=pygame.display.set_mode((800,800))
pygame.display.set_caption("Hangman Game")
FPS=90
clock=pygame.time.Clock()
run=True
green=(0,255,0)
blue=(255,255,255)

# load image
img=[]
for i in range(7):
    y=pygame.image.load(f"images/hangman{str(i)}.png")
    img.append(y)


# game variable
status=0

while run:
    clock.tick(FPS)
    
    win.fill((255,255,255))
    if status==6:
        
        font=pygame.font.Font('freesansbold.ttf',32)
        text=font.render("You lost",True,green,blue)
        textr=text.get_rect()
        textr.center=(400,400)
        win.blit(text,textr)
    else:
        win.blit(img[status],(150,100))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False;
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos();
            if pos and status<7:
                status+=1
            print(pos)
        
        
        
pygame.quit()

    
