import sys
try:
    import pygame, math
except ImportError:
    print('NO PYGAME MODULE FOUND, INSTALL AND TRY AGAIN!!')
    input()
    sys.exit() 
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 1000,400
Screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
background_layer1 = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
background_layer2 = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
backgroudn_layer2.fill((0,0,0,0))

clock = pygame.time.Clock()

transparency = 255
transparency
topColour = (255,255,255)#white
bottomColour = (0,0,0)#black
for y in range(0,HEIGHT):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    intensityTop = y / HEIGHT # Finds how much of the far right colour should be used
    intensityBottom = 1 - intensityTop # Finds how much of the far left colour should be used
    Red_TB = ((intensityTop * topColour[0]) + (intensityBottom * bottomColour[0]))
    Green_TB = ((intensityTop * topColour[1]) + (intensityBottom * bottomColour[1]))
    Blue_TB = ((intensityTop * topColour[2]) + (intensityBottom * bottomColour[2]))
    transparency_TB = (
    
    if Red_TB > 255: # Checks that if the output is more than the max colour that the value is the max colour
        Red_TB = 255
        print('Red above')
    if Green_TB > 255:
        Green_TB = 255
        print('Green above')
    if Blue_TB > 255:
        Blue_TB = 255
        print('Blue above')

    leftColour = (255, 255, 0)#pink
    rightColour = (255,0,255)#yellow
    for x in range(0,WIDTH):
        intensityRight = x / HEIGHT # Finds how much of the far right colour should be used
        intensityLeft = 1 - intensityRight # Finds how much of the far left colour should be used
        Red = ((intensityLeft * leftColour[0]) + (intensityRight * rightColour[0])) # Total of red when two intensities of different colours are crossed
        Green = ((intensityLeft * leftColour[1]) + (intensityRight * rightColour[1])) # Total of green when two intensities of different colours are crossed
        Blue = ((intensityLeft * leftColour[2]) + (intensityRight * rightColour[2])) # Total of blue when two intensities of different colours are crossed
        
        if Red > 255: # Checks that if the output is more than the max colour that the value is the max colour
            Red = 255
            print('Red above')
        if Green > 255:
            Green = 255
            print('Green above')
        if Blue > 255:
            Blue = 255
            print('Blue above')
            
        background_layer2.set_at((x,y), (Red_TB,Green_TB,Blue_TB))
        background_layer1.set_at((x,y), (Red,Green,Blue))
    Screen.blit(background_layer1, (0,0))
    Screen.blit(background_layer2, (0,0))
    pygame.display.update()

count = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Screen.blit(background_layer1, (0,0))
    Screen.blit(background_layer2, (0,0))
    pygame.display.update()
    count += 1
    if count % 500 == 0:
        pygame.event.pump()
        pygame.event.clear()
