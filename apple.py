import pygame
from random import randint
class Apple:
    def changeCoords(self):
        x=randint(1, (780-20)//20)*20
        y=randint(1, (420-20)//20)*20
        self.x = x
        self.y = y
    def __init__(self):    
        self.image = pygame.image.load("images/apple.png")
        self.image = pygame.transform.scale(self.image, (20,20))
        self.changeCoords()
    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))