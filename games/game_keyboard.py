bif = "bg.jpg"  #lot of color use jpg
mif = "mouse.png"  # tranperancy? use png

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)  # creates screen

background = pygame.image.load(bif).convert()   # convert images to loadable format
mouse_c = pygame.image.load(mif).convert_alpha() # transparent 

x, y = 0, 0
movex , movey = 0, 0    # we will add values to movex and movey on pressing keys

while True:
    for event in pygame.event.get():  # to be able to close the screen on clicking x
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                movex =-5
            elif event.key == K_RIGHT:
                movex =+5
            elif event.key == K_UP:
                movey =-5
            elif event.key == K_DOWN:
                movey=+5
				
        if event.type == KEYUP:
            if event.key == K_LEFT:
                movex =0
            elif event.key == K_RIGHT:
                movex =0
            elif event.key == K_UP:
                movey =0
            elif event.key == K_DOWN:
                movey=0
				
	x += movex  # now x value is also incresed
	y +=movey
	
	screen.blit(background, (0,0))
	screen.blit(mouse_c, (x,y))  # this will move mouse image to new values
	
	pygame.display.update()
		