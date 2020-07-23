#Digital Clock
#FILENAME: Main
#AUTHOR: Stephen Fisher
#START DATE: 08/10/12
for module in ['time', 'sys', 'datetime', 'pygame']:
    try:
        exec('import ' + module)
    except ImportError:
        print(module.capitalize(), end = ' ')
        print('Import Failed, Module Not Found')
        input('Quit\n')
        sys.exit()
    
from pygame.locals import *     # import the specifc parts of the modules needed
from datetime import datetime

pygame.init()       # initialise pygame to allow the creation of a screen
WINDOWWIDTH = 700
WINDOWHEIGHT = 300      # create the screen and caption of the window
CAPTION = 'Digital Clock'
Screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption(CAPTION)
Clock = pygame.time.Clock()     #creates a new clock using the pygame time module, this is updated so it begins when the pygame module was initialised

#set up all of the colours that can be used in the game
WHITE = (255, 255, 255)
GREEN = (103, 217, 0)   # background colour
BLACK = (0, 0, 0)
RED = (255,0,0)

class newDotImage:
    def __init__(self, x,y):
        self.xCoord = x
        self.yCoord = y
        self.ON = True
        self.image = self.createDot()

    def createDot(self):
        dot = pygame.Surface((30,30)).convert_alpha()
        dot.fill((0,0,0,0))     # transparent
        pygame.draw.polygon(dot, RED, [(14,0), (15,0), (29,14), (29,15), (15,29), (14,29), (0,15), (0,14)], 0)
        image = pygame.Surface((78,226)).convert_alpha()
        image.fill((0,0,0,0))      # transparent
        image.blit(dot, (24,49))
        image.blit(dot, (24,147))
        return image

class newClockPiece:
    def __init__(self,image, tag, x, y):
        self.image = image
        self.tag = tag
        if self.tag in ['A', 'D', 'G']:
            self.image = pygame.transform.rotate(self.image, 90)
        self.xCoord = x
        self.yCoord = y

class newClockSide:
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        self.image = pygame.Surface((280,226)).convert_alpha()
        self.image.fill((0,0,0,0))
        self.pieceList_Left = []
        self.pieceList_Right = []
        for tag,x,y in [['A', 19,0], ['B', 0,19], ['C', 98,19], ['D', 19,98], ['E', 0,117], ['F', 98,117], ['G', 19,196]]:
            piece1 = newClockPiece(clockPiece, tag, x, y)
            piece2 = newClockPiece(clockPiece, tag, (x+152), y)
            self.pieceList_Left.append(piece1)
            self.pieceList_Right.append(piece2)

        self.neededList_Left = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.neededList_Right = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.edited = True
        self.updateImage()

    def updateImage(self):
        self.image.fill((0,0,0,0))
        for i in range(len(self.pieceList_Left)):
            if self.pieceList_Left[i].tag in self.neededList_Left:
                self.image.blit(self.pieceList_Left[i].image, (self.pieceList_Left[i].xCoord, self.pieceList_Left[i].yCoord))
        for i in range(len(self.pieceList_Right)):
            if self.pieceList_Right[i].tag in self.neededList_Right:
                self.image.blit(self.pieceList_Right[i].image, (self.pieceList_Right[i].xCoord, self.pieceList_Right[i].yCoord))
                
class getClock:
    def __init__(self, pyClock, clockPiece):
        pyClock.tick()      # ticks the clock before getting the current time so that it is as accurate as possible
        
        self.currMilliSec = 0
        self.timeSecond = datetime.now().second
        self.timeMinute = datetime.now().minute
        self.timeHour = datetime.now().hour
        self.dot = newDotImage(311, WINDOWHEIGHT/2 - 113)
        self.hour = newClockSide(31,WINDOWHEIGHT/2 - 113)
        self.minute = newClockSide(389,WINDOWHEIGHT/2 - 113)
        
    def updateTime(self, ms):
        self.currMilliSec += ms
        if self.currMilliSec >= 1000:         # one full second
            self.currMilliSec -= 1000         # removes that second
            self.timeSecond += 1              # adds the second to the seconds counter
            self.dot.ON = not(self.dot.ON)
        if self.timeSecond >= 60:             # one full minute
            self.timeSecond -= 60             # removes that minute
            self.timeMinute += 1              # adds the minute to the minutes counter
            self.minute.edited = True
        if self.timeMinute >= 60:             
            self.timeMinute -= 60             # removes the 60 minutes
            self.timeHour += 1                # adds that to the hour counter
            self.hour.edited = True
        if self.timeHour >= 24:
            self.timeHour -= 24
            self.hour.edited = True
        
        if self.timeMinute < 10:
            str_Min = '0' + str(self.timeMinute)
        else: str_Min = str(self.timeMinute)
        if self.timeHour < 10:
            str_Hour = '0' + str(self.timeHour)
        else: str_Hour = str(self.timeHour)

        return str_Min, str_Hour
    
    def updateImages(self, str_Min, str_Hour):
        str_Min = list(str_Min)
        str_Hour = list(str_Hour)

        if self.minute.edited:
            self.minute.neededList_Left = self.getPiecesPerNum(str_Min[0])
            self.minute.neededList_Right = self.getPiecesPerNum(str_Min[1])
            self.minute.edited = not(self.minute.edited)   
        if self.hour.edited:
            self.hour.neededList_Left = self.getPiecesPerNum(str_Hour[0])             
            self.hour.neededList_Right = self.getPiecesPerNum(str_Hour[1])
            self.hour.edited = not(self.hour.edited)
       
        self.minute.updateImage()
        self.hour.updateImage()

    def getPiecesPerNum(self, num):
        num = int(num)
        tempPieceLi = []
        if num in [0,2,3,5,6,7,8,9]:
            tempPieceLi.append('A')
        if num in [0,4,5,6,8,9]:
            tempPieceLi.append('B')
        if num in [0,1,2,3,4,7,8,9]:
            tempPieceLi.append('C')
        if num in [2,3,4,5,6,8,9]:
            tempPieceLi.append('D')
        if num in [0,2,6,8]:
            tempPieceLi.append('E')
        if num in [0,1,3,4,5,6,7,8,9]:
            tempPieceLi.append('F')
        if num in [0,2,3,5,6,8,9]:
            tempPieceLi.append('G')

        return tempPieceLi

Screen.fill(GREEN)
pygame.display.update()

clockPiece = pygame.Surface((30,90)).convert_alpha()
clockPiece.fill((0,0,0,0))      # transparent
pointList = [(15,0), (29,14), (29,75), (15,89), (14,89), (0,75), (0,14), (14,0)]#specific coords 
pygame.draw.polygon(clockPiece, RED, pointList, 0)

background = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT)).convert_alpha()
background.fill(GREEN)      # transparent
displayClock = getClock(Clock, clockPiece)
#-----------------RUNNING CODE STARTS HERE-----------------#
count = 0
while True:
    for event in pygame.event.get(QUIT):
        pygame.quit()   # if so it properly shuts down pygame and then the application
        sys.exit()
            
    ms = Clock.tick()
    print(ms)
    str_Min, str_Hour = displayClock.updateTime(ms)     #update clock here
    displayClock.updateImages(str_Min, str_Hour)        #update clock image here.

    Screen.blit(background, (0,0))
    Screen.blit(displayClock.hour.image, (displayClock.hour.xCoord, displayClock.hour.yCoord))
    if displayClock.dot.ON:
        Screen.blit(displayClock.dot.image, (displayClock.dot.xCoord, displayClock.dot.yCoord))
    Screen.blit(displayClock.minute.image, (displayClock.minute.xCoord, displayClock.minute.yCoord))
    
    pygame.display.update()
    pygame.display.set_caption(CAPTION + '| FPS ' + str(Clock.get_fps()))
    count += 1       # adds 1 to the loop counter
    pygame.event.clear(MOUSEMOTION)     # these events are created when the mouse is moved and are very frequent
    if count % 25 == 0:     # if the loop counter is any multiple of 25 it clears the event queue
        pygame.event.pump()
        pygame.event.clear()
