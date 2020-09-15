import pygame
import sys
from score import loadScore, saveScore
font = pygame.font.SysFont("arialrounded", 30)
bgcolor = (0,128,0)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def draw_text(text, font, color, screen, x, y):
    textobj = font.render(text, 1, color)
    text_rect = textobj.get_rect(center=(x,y))
    screen.blit(textobj, text_rect)


def mainMenu(screen):
    from game import game
    bg = Background("images/bg.jpg", [0,0])
    click = False
    while True:
 
        screen.fill(bgcolor)
        #screen.blit(bg.image, bg.rect)
        draw_text('Snake', font, (0,0,0), screen, 780/2, 420/5)
        draw_text("Highscore: "+str(loadScore())+" score", pygame.font.SysFont("arialrounded", 24), (0,0,0), screen, 780/2, 420/5*1.75)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_1.center=(780/2, 420/5*2.75)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_2.center=(780/2, 420/5*3.75)
        if button_1.collidepoint((mx, my)):
            if click:
                game(screen)
        #if button_2.collidepoint((mx, my)):
        #    if click:
        #        options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        draw_text("Play", font, (0,0,0), screen, 780/2, 420/5*2.75)
        draw_text("Options", font, (0,0,0), screen, 780/2, 420/5*3.75)
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()

def gameOverMenu(screen, score):
    from game import game
    click = False
    if score>loadScore():
        saveScore(score)
    while True:
        screen.fill(bgcolor)
        #screen.blit(bg.image, bg.rect)
        draw_text('Game Over', font, (0,0,0), screen, 780/2, 420/5)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_1.center=(780/2, 420/5*3)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_2.center=(780/2, 420/5*4)
        if button_1.collidepoint((mx, my)):
            if click:
                game(screen)
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        score_str = "Score: "+str(score)
        if score>loadScore():
            score_str+=" (NEW HIGHSCORE!)"
        draw_text(score_str, font, (0,0,0), screen, 780/2, 420/5*2)
        draw_text("Play again", font, (0,0,0), screen, 780/2, 420/5*3)
        draw_text("Quit", font, (0,0,0), screen, 780/2, 420/5*4)
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()