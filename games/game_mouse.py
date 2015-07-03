bif = "bg.jpg"  #lot of color use jpg
mif = "mouse.png"  # tranperancy? use png

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)  # creates screen

background = pygame.image.load(bif).convert()   # convert images to loadable format
mouse_c = pygame.image.load(mif).convert_alpha() # transparent 

while True:
    for event in pygame.event.get():  # to be able to close the screen on clicking x
	    if event.type == QUIT:
		    pygame.quit()
		    sys.exit()
			
    screen.blit(background, (0,0))   # blit means copy
	
    x,y = pygame.mouse.get_pos()   # position of mouse copied in x and y
    x -= mouse_c.get_width() /2
    y -= mouse_c.get_height() / 2
	
    screen.blit(mouse_c, (x, y))
	
    pygame.display.update()  # update 