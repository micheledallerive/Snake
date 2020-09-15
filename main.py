import pygame

pygame.init()

from menus import mainMenu
from game import game


#pygame.time.Clock().tick(1)

(width, height) = (780,420)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
pygame.display.flip()

mainMenu(screen) 