import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)  # creates screen
points = [ (20,120), (140,140), (110, 30), (120,120), (240,140), (310, 30)]
color = (255, 255, 0)
color2 = (230, 170, 0)
position=(300, 300)
radius=(60)


while True:
	for event in pygame.event.get():  # to be able to close the screen on clicking x
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
# for shapes, you  need to lock the screen
	screen.lock()
	pygame.draw.rect(screen, (140,240,130), Rect((100,100),(130, 150)))
	pygame.draw.polygon(screen, color, points)
	pygame.draw.circle(screen, color, position, radius)
	screen.unlock()		

	pygame.display.update()
		