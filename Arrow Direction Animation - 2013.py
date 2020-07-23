import pygame, sys, time, random, math
from pygame.locals import *
from math import *
pygame.init()

# for those who can be bothered fiddle with these bits and see the effect
#\/\/\/\/\/\/\/\/\/\/\/\/\/\
WINDOWWIDTH = 1500
WINDOWHEIGHT = 900
BLOCKWIDTH = 10
BLOCKHEIGHT = 30
MOVESPEED = 5
NUM_OF_BLOBS = 10
NUM_BLOBS_ADD = 490
SMALLRECTWIDTH = 2 
SMALLRECTHEIGHT = 30
#\/\/\/\/\/\/\/\/\/\/\/\/\/\
Screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
GRAD = math.pi / 180
'''
redImage = pygame.image.load('Project Files/Animation/RedBlob.png').convert_alpha()
blueImage = pygame.image.load('Project Files/Animation/BlueBlob.png').convert_alpha()
greenImage = pygame.image.load('Project Files/Animation/GreenBlob.png').convert_alpha()
yellowImage = pygame.image.load('Project Files/Animation/YellowBlob.png').convert_alpha()
orangeImage = pygame.image.load('Project Files/Animation/OrangeBlob.png').convert_alpha()
'''
redImage = pygame.image.load('Project Files/Animation/RedBlob_Black.png').convert()
blueImage = pygame.image.load('Project Files/Animation/BlueBlob_Black.png').convert()
greenImage = pygame.image.load('Project Files/Animation/GreenBlob_Black.png').convert()
yellowImage = pygame.image.load('Project Files/Animation/YellowBlob_Black.png').convert()
orangeImage = pygame.image.load('Project Files/Animation/OrangeBlob_Black.png').convert()
Images = [redImage, blueImage, greenImage, yellowImage, orangeImage]

class Blob:
    def __init__(self, Images):
        self.currCoords = [WINDOWWIDTH/2, WINDOWHEIGHT/2]
        pie = int(math.pi)
        self.speed = MOVESPEED
        self.dx = randNum(-pie, pie)
        self.dy = randNum(-pie, pie)
        self.angle = 0
        self.image_Orig = randImage(Images)
        
    def updatePos(self, sec):
        self.currCoords[0] += self.dx
        self.currCoords[1] += self.dy
            
    def updateGrad(self, XY):
        self.dx = ((XY[0] - self.currCoords[0])) * sec
        self.dy = ((XY[1] - self.currCoords[1])) * sec
        self.hypo = sqrt((self.dx**2) + (self.dy**2))#creates the length of the hypotenuse to allow the use of a ratio

        self.updateAim()
        self.updateAngle()

    def updateAngle(self):
        self.angle = math.atan2(-self.dx, -self.dy)/math.pi*180.0
        self.image = pygame.transform.rotate(self.image_Orig, self.angle)

    def updateAim(self):
        ratio = 10 / self.hypo
        self.dx *= ratio
        self.dy *= ratio
        
def randImage(Images):
    return Images[random.randint(0,4)]

def randNum(a,b):
    return(random.randint(a,b))

def mousePos():
    x,y = pygame.mouse.get_pos()
    return [x, y]

blocks = []
for i in range(NUM_OF_BLOBS):
    B = Blob(Images)
    B.updateAngle()
    blocks.append(B)
 
loop = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            XY = mousePos()
            for B in blocks:
                B.updateGrad(XY)
                B.updateAngle()

    if loop % 5 == 1 and NUM_BLOBS_ADD != 0:
        B = Blob(Images)
        B.updateAngle()
        blocks.append(B)
        NUM_BLOBS_ADD -= 1

    ms = clock.tick()
    sec = ms / 1000  
    Screen.fill(BLACK)
    for B in blocks:
        B.updatePos(sec)
        if (B.currCoords[0] < 0) or (B.currCoords[0] > (WINDOWWIDTH - BLOCKWIDTH)):
            B.dx = (-B.dx)
            B.updateAngle()
        if (B.currCoords[1] < 0) or (B.currCoords[1] > (WINDOWHEIGHT - BLOCKHEIGHT)):
            B.dy = (-B.dy)
            B.updateAngle()
        x = int(B.currCoords[0])
        y = int(B.currCoords[1])
        Screen.blit(B.image, (x, y))

    pygame.display.update()
    time.sleep(0.02)
    loop += 1
