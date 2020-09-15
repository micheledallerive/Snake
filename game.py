import pygame
from snake import Snake
from apple import Apple
import time
import sys
bgcolor = (0,128,0)

font = pygame.font.SysFont("arialrounded", 30)
def draw_text(text, font, color, screen, x, y):
    textobj = font.render(text, 1, color)
    text_rect = textobj.get_rect(center=(x,y))
    screen.blit(textobj, text_rect)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def pause(screen):
    running = True
    s = pygame.Surface((780,420))  # the size of your rect
    s.set_alpha(69)                # alpha level
    s.fill((0,0,0))                          # notice the alpha value in the color
    while running:
        screen.blit(s, (0,0))
        draw_text("Pause", font, (255,255,255), screen, 780/2, 420/3)
        click=False
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_1.center=(780/2, 420/5*3)
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        mx, my = pygame.mouse.get_pos()
        draw_text("Resume", font, (255,255,255), screen, 780/2, 420/5*3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if button_1.collidepoint((mx, my)):
            if click:
                running=False
        pygame.display.update()

def gameOver(screen, score):
    # TODO SAVE score
    from menus import gameOverMenu
    gameOverMenu(screen, score)

def drawscore(screen, score):
    text = font.render("Score: "+str(score), False, (0,0,0))
    screen.blit(text, (10,0))

def game(screen):
    move=False
    score=0
    running = True
    snake = Snake(screen)
    apple = Apple()
    bg = Background("images/bg.jpg", [0,0])
    while running:
        clickedArrow=False
        ateApple=False
        screen.fill(bgcolor)
        #screen.blit(bg.image, bg.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause(screen)
                    continue 
                if event.key == pygame.K_UP and snake.direction!=2 and not clickedArrow:
                    move=True
                    clickedArrow=True
                    snake.setDirection(0)
                if event.key == pygame.K_RIGHT and snake.direction!=3 and not clickedArrow:
                    move=True
                    clickedArrow=True
                    snake.setDirection(1)
                if event.key == pygame.K_DOWN and snake.direction!=0 and not clickedArrow:
                    move=True
                    clickedArrow=True
                    snake.setDirection(2)
                if event.key == pygame.K_LEFT and snake.direction!=1 and not clickedArrow:
                    move=True
                    clickedArrow=True
                    snake.setDirection(3)
                if event.key == pygame.K_1:
                    snake.makeBigger()
                    score+=1
                    ateApple=True
                if event.key == pygame.K_2:
                    snake.makeSmaller()
        if move:
            snake.move()
        if snake.pieces[0].x==apple.x and snake.pieces[0].y==apple.y:
            score+=1
            apple.changeCoords()
            snake.makeBigger()
            ateApple=True
        if snake.isDead() and not ateApple:
            gameOver(screen, score)
            running=False
        apple.draw(screen)
        if not ateApple: 
            snake.draw()
        drawscore(screen, score)
        pygame.display.update()
        time.sleep(.25)