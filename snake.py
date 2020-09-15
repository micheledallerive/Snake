import pygame

MOVE_SIZE=20
SNAKE_COLOR = (255,255,255)

def getRotateImage(image, direction):
    img = pygame.image.load("images/snake_sprite/"+image+".png")
    angle=direction*90
    if direction==-1:
        angle=0
    if direction==1:
        angle=90*3
    if direction==3:
        angle=90
    return pygame.transform.rotate(img, angle)

def getCurve(beforeDirection, afterDirection):
    #print(beforeDirection, afterDirection)
    a=0
    if beforeDirection==0:
        if afterDirection==1:
            a=3
    if beforeDirection==1:
        if afterDirection==0:
            a=1
    if beforeDirection==2:
        if afterDirection==1:
            a=2
        else:
            a=1
    if beforeDirection==3:
        if afterDirection==0:
            a=2
        else:
            a=3

    return getRotateImage("curve", a)

def draw_text(text, color, screen, x, y, font = pygame.font.SysFont("arialrounded", 20)):
    textobj = font.render(text, 1, color)
    text_rect = textobj.get_rect(topleft=(x,y))
    screen.blit(textobj, text_rect)

class SnakePiece:
    def __init__(self, x, y, direction, curved=False, bd=0, ad=0):
        self.x=x
        self.y=y
        if direction==0:
            self.y-=MOVE_SIZE
        if direction==1:
            self.x-=MOVE_SIZE
        if direction==2:
            self.y+=MOVE_SIZE
        if direction==3:
            self.x+=MOVE_SIZE
        self.curved=curved
        self.bd=bd
        self.ad=ad
        self.direction=direction
    def move(self):
        if self.direction==0:
            self.y-=MOVE_SIZE
        if self.direction==1:
            self.x+=MOVE_SIZE
        if self.direction==2:
            self.y+=MOVE_SIZE
        if self.direction==3:
            self.x-=MOVE_SIZE
    def compareDirection(self, otherPiece):
        if(self.x>otherPiece.x):
            return 3
        if(self.x<otherPiece.x):
            return 1
        if(self.y>otherPiece.y):
            return 0
        if(self.y<otherPiece.y):
            return 2

def needsToBeCurved(pieces, i):
    if i-1<0:
        return False
    before = pieces[i-1]
    after = pieces[i+1]
    if not before.x==after.x and not before.y==after.y:
        return True
    return False

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.pieces=[SnakePiece(780/20//2*20,420/20//2*20,1)]
        self.direction=1 # 0 NORD 1 EST 2 SUD 3 OVEST
        self.size=1
        self.makeBigger()
    def makeSmaller(self):
        if(self.size>2):
            self.pieces.remove(self.pieces[self.size-1])
            self.size-=1
    def makeBigger(self):
        if(self.size==1): # there is only the head
            head = self.pieces[0]
            self.pieces.append(SnakePiece(head.x, head.y, head.direction))
        else:
            tail = self.pieces[self.size-1] # tail piece
            piece = SnakePiece(tail.x, tail.y, tail.direction)
            self.pieces.append(piece)
        self.size+=1
        self.draw()
    def setDirection(self, dir):
        if self.direction!=dir:    
            self.direction = dir
            self.pieces[0].curved=True
    def move(self): 
        self.pieces[0].direction=self.direction
        for i in range(self.size-1, 0, -1):
            piece = self.pieces[i]
            #print("Piece #"+str(i)+": ", piece.direction, piece.x, piece.y, piece.curved)
            if not piece.curved:
                piece.direction=self.pieces[i-1].direction
            if i==self.size-1:
                piece.direction=self.pieces[i-1].direction
            piece.x=self.pieces[i-1].x
            piece.y=self.pieces[i-1].y
            piece.curved=self.pieces[i-1].curved
            if piece.curved and i<self.size-1:
                beforeDirection = self.pieces[i-1].direction
                afterDirection = self.pieces[i+1].direction
                piece.bd=beforeDirection
                piece.ad=afterDirection
            self.pieces[i-1].curved=False
        self.pieces[0].move()
    def draw(self):
        for i in range(0, self.size):
            piece = self.pieces[i]
            #print(piece.direction, piece.x, piece.y)
            if i==0:
                self.screen.blit(getRotateImage("head", piece.direction), (piece.x, piece.y))
            else:
                if i==self.size-1:
                    self.screen.blit(getRotateImage("tail", piece.direction), (piece.x, piece.y))
                else:  
                    if piece.curved:
                        self.screen.blit(getCurve(piece.bd, piece.ad), (piece.x, piece.y))
                    else:
                        self.screen.blit(getRotateImage("piece", piece.direction), (piece.x, piece.y))
            #DEBUG TEXT
            #draw_text(str(piece.direction), (255,0,0), self.screen, piece.x, piece.y)

    def isDead(self):
        if self.pieces[0].x<0 or self.pieces[0].x>=780 or self.pieces[0].y<0 or self.pieces[0].y>=420:
            return True
        for i in range(1, self.size):
            piece=self.pieces[i]
            if self.pieces[0].x==piece.x and self.pieces[0].y==piece.y:
                return True
        return False