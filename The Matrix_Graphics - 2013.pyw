#The Matrix_V2 (Graphics)    #AUTHOR: Stephen Fisher
#FILENAME: The Matrix_Graphics    #AUTHOR: Stephen Fisher
#AUTHOR: Stephen Fisher    #AUTHOR: Stephen Fisher
#START DATE: 08/05/2013    #AUTHOR: Stephen Fisher
    #AUTHOR: Stephen Fisher
for module in ['time','sys','random','pygame']:    #AUTHOR: Stephen Fisher
    try:    #AUTHOR: Stephen Fisher
        exec('import ' + module)    #AUTHOR: Stephen Fisher
    except ImportError:    #AUTHOR: Stephen Fisher
        print(module.capitalize(), end = ' ')    #AUTHOR: Stephen Fisher
        print('Import Failed, Module Not Found')    #AUTHOR: Stephen Fisher
        input('Quit\n')    #AUTHOR: Stephen Fisher
        sys.exit()    #AUTHOR: Stephen Fisher
from pygame.locals import *#import pygame first to be able to display graphics    #AUTHOR: Stephen Fisher
    #AUTHOR: Stephen Fisher
pygame.init()#initialise pygame to allow the creation of a screen    #AUTHOR: Stephen Fisher
WINDOWWIDTH = 300     #AUTHOR: Stephen Fisher
WINDOWHEIGHT = 210#create the screen and caption of the window    #AUTHOR: Stephen Fisher
CAPTION = 'THE MATRIX'    #AUTHOR: Stephen Fisher
Screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.DOUBLEBUF|pygame.RESIZABLE, 32)    #AUTHOR: Stephen Fisher
Clock = pygame.time.Clock()#creates a new clock using the pygame time module, this is updated so it begins when the pygame module was initialised    #AUTHOR: Stephen Fisher
    #AUTHOR: Stephen Fisher
letterFont = pygame.font.SysFont(None, 30)    #AUTHOR: Stephen Fisher
#set up all of the colours that can be used in the game    #AUTHOR: Stephen Fisher
GREEN = (103, 217, 0)#background colour    #AUTHOR: Stephen Fisher
BLACK = (0, 0, 0)    #AUTHOR: Stephen Fisher
RED = (255, 0, 0)    #AUTHOR: Stephen Fisher
class newLetter:    #AUTHOR: Stephen Fisher
    def __init__(self, x, letter, speed, refreshSpeed):    #AUTHOR: Stephen Fisher
        self.x = x    #AUTHOR: Stephen Fisher
        self.y = -21    #AUTHOR: Stephen Fisher
        self.speed = speed    #AUTHOR: Stephen Fisher
        self.refreshSpeed = refreshSpeed    #AUTHOR: Stephen Fisher
        self.letterChangeCount = 0    #AUTHOR: Stephen Fisher
        self.distMoved = 0    #AUTHOR: Stephen Fisher
        self.image = letterFont.render(str(letter), True, GREEN)    #AUTHOR: Stephen Fisher
        self.changeLetter(letter)    #AUTHOR: Stephen Fisher
        self.setSpawned(False)    #AUTHOR: Stephen Fisher
    def getX(self):    #AUTHOR: Stephen Fisher
        return self.x    #AUTHOR: Stephen Fisher
    def getY(self):    #AUTHOR: Stephen Fisher
        return int(self.y)    #AUTHOR: Stephen Fisher
    def getImage(self):    #AUTHOR: Stephen Fisher
        return self.image    #AUTHOR: Stephen Fisher
    def getHeight(self):    #AUTHOR: Stephen Fisher
        return self.image.get_height()    #AUTHOR: Stephen Fisher
    def getWidth(self):    #AUTHOR: Stephen Fisher
        return self.image.get_width()    #AUTHOR: Stephen Fisher
    def getSpeed(self):    #AUTHOR: Stephen Fisher
        return self.speed    #AUTHOR: Stephen Fisher
    def getDistMoved(self):    #AUTHOR: Stephen Fisher
        return int(self.distMoved)    #AUTHOR: Stephen Fisher
    def setSpawned(self, boolean):    #AUTHOR: Stephen Fisher
        self.spawned = boolean    #AUTHOR: Stephen Fisher
    def updateY(self):    #AUTHOR: Stephen Fisher
        self.y += self.speed    #AUTHOR: Stephen Fisher
        self.distMoved += self.speed    #AUTHOR: Stephen Fisher
    def changeLetter(self, letter):    #AUTHOR: Stephen Fisher
        self.letterChangeCount += 1    #AUTHOR: Stephen Fisher
        if self.letterChangeCount == self.refreshSpeed:    #AUTHOR: Stephen Fisher
            self.image = letterFont.render(str(letter), True, GREEN)    #AUTHOR: Stephen Fisher
            self.letterChangeCount = 0    #AUTHOR: Stephen Fisher
    def checkForSpawn(self):    #AUTHOR: Stephen Fisher
        if (self.getHeight() <= self.getY() <= (self.getHeight() * 1.5)) and not self.spawned:    #AUTHOR: Stephen Fisher
            letter.setSpawned(True)    #AUTHOR: Stephen Fisher
            return True    #AUTHOR: Stephen Fisher
        return False    #AUTHOR: Stephen Fisher
    def checkForRemove(self):    #AUTHOR: Stephen Fisher
        if (self.getDistMoved() >= WINDOWHEIGHT + self.getHeight()) or (self.getX() >= WINDOWWIDTH + self.getWidth()):    #AUTHOR: Stephen Fisher
            return True    #AUTHOR: Stephen Fisher
        return False    #AUTHOR: Stephen Fisher
def getWidthOfLetters():    #AUTHOR: Stephen Fisher
    letterLi = []    #AUTHOR: Stephen Fisher
    for i in range(int(WINDOWWIDTH/15)):    #AUTHOR: Stephen Fisher
        letterLi.append(newLetter((i*15), random.choice(alphabet), random.uniform(1,3), random.choice([0,3,4,5])))    #AUTHOR: Stephen Fisher
        letterLi.append(newLetter((i*15), random.choice(alphabet), random.uniform(1,3), random.choice([0,3,4,5])))    #AUTHOR: Stephen Fisher
    return letterLi    #AUTHOR: Stephen Fisher
#-----------------RUNNING CODE STARTS HERE-----------------#    #AUTHOR: Stephen Fisher
Screen.fill(BLACK)    #AUTHOR: Stephen Fisher
count = 0    #AUTHOR: Stephen Fisher
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']    #AUTHOR: Stephen Fisher
letterLi = getWidthOfLetters()    #AUTHOR: Stephen Fisher
tempLi = []    #AUTHOR: Stephen Fisher
    #AUTHOR: Stephen Fisher
while True:    #AUTHOR: Stephen Fisher
    for event in pygame.event.get():    #AUTHOR: Stephen Fisher
        if event.type == QUIT:#searches the event queue to see if the close button has been clicked    #AUTHOR: Stephen Fisher
            pygame.quit()#if so it properly shuts down pygame and then the application    #AUTHOR: Stephen Fisher
            sys.exit()    #AUTHOR: Stephen Fisher
    #AUTHOR: Stephen Fisher
        elif event.type == VIDEORESIZE:    #AUTHOR: Stephen Fisher
            WINDOWWIDTH = event.w; WINDOWHEIGHT = event.h    #AUTHOR: Stephen Fisher
            letterLi = getWidthOfLetters()    #AUTHOR: Stephen Fisher
            Screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.DOUBLEBUF|pygame.RESIZABLE, 32)    #AUTHOR: Stephen Fisher
                #AUTHOR: Stephen Fisher
    ms = Clock.tick(50)    #AUTHOR: Stephen Fisher
    Screen.fill(BLACK)    #AUTHOR: Stephen Fisher
    for letter in letterLi[:]:    #AUTHOR: Stephen Fisher
        letter.updateY()    #AUTHOR: Stephen Fisher
        Screen.blit(letter.getImage(), (letter.getX(), letter.getY()))    #AUTHOR: Stephen Fisher
        letter.changeLetter(random.choice(alphabet))    #AUTHOR: Stephen Fisher
            #AUTHOR: Stephen Fisher
        if letter.checkForSpawn(): letterLi.append(newLetter(letter.getX(), random.choice(alphabet), random.uniform(1,3), random.choice([0,3,4,5])))    #AUTHOR: Stephen Fisher
        if letter.checkForRemove(): letterLi.remove(letter)    #AUTHOR: Stephen Fisher
        #AUTHOR: Stephen Fisher
    pygame.display.flip()    #AUTHOR: Stephen Fisher
    pygame.display.set_caption(CAPTION + ' | FPS %.0f' % Clock.get_fps())    #AUTHOR: Stephen Fisher
    count += 1#adds 1 to the loop counter    #AUTHOR: Stephen Fisher
    pygame.event.clear(MOUSEMOTION)#these events are created when the mouse is moved and are very frequent    #AUTHOR: Stephen Fisher
    if count % 50 == 0:#if the loop counter is any multiple of 25 it clears the event queue    #AUTHOR: Stephen Fisher
        pygame.event.pump()    #AUTHOR: Stephen Fisher
        pygame.event.clear()    #AUTHOR: Stephen Fisher
