import pygame, sys
from pygame.locals import *#import pygame first to be able to display graphics

pygame.init()#initialise pygame to allow the creation of a screen
WINDOWWIDTH = 700
WINDOWHEIGHT = 200#create the screen and caption of the window
CAPTION = 'CAPTION HERE'
Screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption(CAPTION)

Clock = pygame.time.Clock()#creates a new clock using the pygame time module, this is updated so it begins when the pygame module was initialised

GREEN = (103, 217, 0)#background colour
BLACK = (0, 0, 0)

#-----------------RUNNING CODE STARTS HERE-----------------#

def addNewLED(n, Screen):
    pygame.draw.rect(Screen, GREEN, ((n-1)*100, 0, 100, 200))
    pygame.display.update()


count = 0
n = 0
Clock.tick()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:#searches the event queue to see if the close button has been clicked
            pygame.quit()#if so it properly shuts down pygame and then the application
            sys.exit()
            
    count += Clock.tick()
    if count >= 40:
        count -= 40
        n += 1
        addNewLED(n, Screen)
        
    if n == 7:
        n = 0
        pygame.time.wait(250) # 250 ms
        Clock.tick()
        Screen.fill(BLACK)
        pygame.display.update()
        pygame.event.pump()
        pygame.event.clear()
        
