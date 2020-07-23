#Block Dodger Game
#Author Stephen Fisher, help from Roberto Dyke

import pygame, sys, time, random
from pygame.locals import *
pygame.init()
Clock = pygame.time.Clock()#creates a new clock

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
Screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Block Dodger Game')
playerRectSize = 16
playerMaxList = 15
menuButtons = []

BLACK = (0, 0, 0)#regular colours
GREY = (195, 195, 195)
#\/\/ rect colours
RED = (255, 0, 0)
PURPLE = (153, 0, 153)
ORANGE = (255, 153, 0)
YELLOW = (255, 255, 0)
GREEN = (51, 255, 0)
BLUE = (0, 0, 255)
BROWN = (153, 102, 51)
#\/\ background colours
WHITE = (255, 255, 255)
PALEBLUE = (0, 255, 255)
PINK = (255, 102, 255)
LIGHTBROWN = (255, 204, 204)

basicFont = pygame.font.SysFont(None, 120)
titleFont = pygame.font.SysFont(None, 80)
smallFont = pygame.font.SysFont(None, 40)
tinyFont = pygame.font.SysFont(None, 16)

class getClock:
    def __init__(self):
        self.milliSec = 0
        self.sec = 0
        self.min = 0
        self.sleep_sec = 0.00001
        self.sleep_rect = 0.0001

class scoreText:
    def __init__(self, xCoord, yCoord, score, time):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.colour = (0,0,0)
        self.timeLeft = time
        self.totalTime = time
        self.score = score
        self.fadeColour()
        
    def fadeColour(self):
        if self.colour[0] < 250:
            R = self.colour[0] + 10
        else: R = 255
        if self.colour[1] < 250:
            G = self.colour[1] + 10
        else: G = 255
        if self.colour[2] < 250:
            B = self.colour[2] + 10
        else: B = 255

        
        self.colour = (R,G,B)
        self.text, self.textRect = textCreator(('+' + str(self.score)), 'tiny', self.colour)

        self.yCoord -= 1#makes the text rise up while disappearing

class getButton:
    def __init__(self, string, font, colour, X, Y, command):
        self.text, self.textRect = textCreator(string, font, colour)
        self.xCoord = X - (self.textRect.width/2)
        self.yCoord = Y
        self.textRect.left = self.xCoord
        self.textRect.top = self.yCoord
        self.command = command

    def blit(self, Screen):
        Screen.blit(self.text, ((self.xCoord, self.yCoord)))

class newPlayer:
    def __init__(self, playerRectSize, playerMaxList, gameMode):
        self.clock = getClock()
        self.score = 0#points are added for each second and for each collision with a good rect
        self.rectScore = 0
        self.timeScore = 0
        self.numCollisions = 0
        self.gameMode = gameMode
        self.Rect = newRect(playerRectSize, BLACK, self)#16 pixel wide square
        self.list_max_len = playerMaxList
        self.ScreenRect = pygame.Rect(0, 0, WINDOWWIDTH, WINDOWHEIGHT)
        self.sleep = 0.03#time to sleep between each loop smaller time faster game
        self.fullScreen = False
        self.invincible = False
        self.invincible_timer = 0
        self.currPower = False
        self.chanceList = [False] * 14
        self.chanceList.append(True)

    def updateMousePos(self):
        XY = getMousePos()
        self.Rect.rect.centerx = XY[0]#left side of the rect is along the x axis
        self.Rect.rect.centery = XY[1]#top side of the rect is along the y axis

    def resetScores(self, gameMode):
        self.clock = getClock()
        self.score = 0#points are added for each second and for each collision with a good rect
        self.rectScore = 0
        self.timeScore = 0
        self.numCollisions = 0
        self.sleep = 0.03#time to sleep between each loop smaller time faster game
        self.gameMode = gameMode

    def updateClock(self, ms):
        player.clock.milliSec += ms#adds the new number of milliseconds to the overall clock
        if player.clock.milliSec >= 1000:#if a second or more has passed
            player.clock.milliSec -= 1000#removes a full second from the time
            player.clock.sec += 1#adds that second to the seconds counter
            player.score += 1#also adds one to the player score
            player.timeScore += 1
            player.sleep -= player.clock.sleep_sec#makes the sleep time shorter and thus speeds up the program
        if player.clock.sec >= 60:
            player.clock.min += 1
            player.clock.sec -= 60
        if player.invincible_timer > 0:
            player.invincible_timer -= ms
        if player.invincible_timer <= 0:
            player.invincible_timer = 0
            player.invincible = False
            player.currPower = False

class newRect:
    def __init__(self, size, colour, player):
        if colour == RED:
            self.type = 'bad'#you need to avoid the red rects so they are termed 'bad' with the black ones being 'good'
        else: self.type = 'good'
        self.getSize(size)
        self.colour = colour
        self.speed = random.randint(2,5)#3 and 7 are the upper and lower bounds for the number of pixels to add each frame
        if size != 'large' and size != 'small':
            self.xCoord = WINDOWWIDTH/2
            self.yCoord = WINDOWHEIGHT/2
        else: self.getDirections()
        if size != 'large' and size != 'small':
            powerupChance = False
        else:
            powerupChance = random.choice(player.chanceList)
        if self.type == 'good' and player.gameMode == 'powerup' and powerupChance and player.currPower == False:
            self.powerup = random.choice(['speed', 'points', 'invincibility'])
            player.currPower = True
        else:
            self.powerup = None
        

    def updatePos(self, RectList, Screen):
        if self.up_down == True:#if moving up or down only the y coord changes as the x position doesnt change
            self.yCoord += self.speed
        else: self.xCoord += self.speed
        self.rect.left = self.xCoord
        self.rect.top = self.yCoord
        if not(self.rect.colliderect(Screen)):#makes sure some part of it is on the screen and if not removes it from the list
            RectList.remove(self)

    def getDirections(self):
        self.up_down = random.choice([True, False])#is the rect moving up/down if not its moving left/right
        if self.up_down == True:#it is moving up or down
            self.xCoord = random.randint(0,(WINDOWWIDTH - self.rect.width))
            if random.choice([True, False]) == True:#it is moving left
                self.yCoord = WINDOWHEIGHT
                self.speed = (-self.speed)
            else: self.yCoord = 1 - self.rect.height#it is moving right
        else:#it is moving left or right
            self.yCoord = random.randint(0,(WINDOWHEIGHT - self.rect.height))
            if random.choice([True, False]) == True:#it is moving up
                self.xCoord = WINDOWWIDTH
                self.speed = (-self.speed)
            else: self.xCoord = 1 - self.rect.width#it is moving down

    def getSize(self, size):
        if size == 'large':
            length = random.randint(17,32)
        elif size == 'small':
            length = random.randint(8,16)
        else:length = size#for the first rect(the players) I want it to be personally adjustable not random, so I put in the correct values
        self.rect = pygame.Rect(0, 0, length, length)#uses length because its a square and therefore length is both the width and height
        self.size = size

def textCreator(string, font, colour):
    try:
        if font == 'basic':
            temp = basicFont.render(string, True, colour)
        elif font == 'title':
            temp = titleFont.render(string, True, colour)
        elif font == 'small':
            temp = smallFont.render(string, True, colour)
        elif font == 'tiny':
            temp = tinyFont.render(string, True, colour)
        tempRect = temp.get_rect()
    except UnboundLocalError:#if the wrong text style has been specified it doesnt crash but puts this message
        temp = tinyFont.render('Invalid Text Style!!', True, BLACK)
        tempRect = temp.get_rect()
    temp.convert_alpha()
    return temp, tempRect

def getHighscores(player):
    highscores = []
    try:
        if player.gameMode == 'psycho':
            file = open('Project Files\Block Dodger\Block Dodger Game Highscores - Psycho.txt', 'r')
        elif player.gameMode == 'powerup':
            file = open('Project Files\Block Dodger\Block Dodger Game Highscores - PowerUps.txt', 'r')
        else: file = open('Project Files\Block Dodger\Block Dodger Game Highscores.txt', 'r')
        for line in file:
            highscores.append(int(line))
    except IOError:
        pass
    while len(highscores) < 5:
        highscores.append(0)
    return highscores

def updateHighscores(highscores, player):
    highscores.append(player.score)
    highscores.sort()
    if len(highscores) > 6:
        highscores.remove(highscores[0])
    highscores.sort(reverse = True)
    return highscores

def returnHighscores(highscores, player):
    highscores.sort()
    if len(highscores) > 5:
        highscores.remove(highscores[0])
    if player.gameMode == 'psycho':
        file = open('Project Files\Block Dodger\Block Dodger Game Highscores - Psycho.txt', 'w')
    elif player.gameMode == 'powerup':
        file = open('Project Files\Block Dodger\Block Dodger Game Highscores - PowerUps.txt', 'w')
    else: file = open('Project Files\Block Dodger\Block Dodger Game Highscores.txt', 'w')
    for i in highscores:
        file.write(str(i) + '\n')

def displayEndGame(player):
    #\/\/\/\/\/\/\/\/\/\ creating the end game message text parts
    highscores = getHighscores(player)
    highscores = updateHighscores(highscores, player)
    X = int(WINDOWWIDTH/2)
    Y = 20
    text = []
    text.append(getButton('Game Over!', 'basic', BLACK, X, Y, None))#basic, title, small, tiny
    Y += 85
    if player.gameMode == 'psycho':
        text.append(getButton('Highscores - Psycho', 'small', GREY, X, Y, None))
    elif player.gameMode == 'powerup':
        text.append(getButton('Highscores - PowerUps', 'small', GREY, X, Y, None))
    else: text.append(getButton('Highscores', 'title', GREY, X, Y, None))
    Y += 65
    for i in range(len(highscores)):#five highscores total
        text.append(getButton(str(highscores[i]), 'small', GREY, X, Y, None))
        Y += 45
        if i == 4:#the second last item in the list
            tempX1 = int(WINDOWWIDTH/4)
            tempX2 = int(WINDOWWIDTH*(3/4))
            tempY = Y - 10
        if int(highscores[i]) == int(player.score):
            pointerRect = pygame.Rect((WINDOWWIDTH/4) + 20, (Y -40), 50, 10)            
    text.append(getButton('Menu', 'title', GREY, X, (WINDOWWIDTH - 65), 'menu'))
    if player.clock.sec < 10:
        sec = '0' + str(player.clock.sec)
    else: sec = str(player.clock.sec)
    text.append(getButton((str(player.clock.min) + ':' + str(sec)), 'tiny', BLACK, X, Y, None))
    Y += 25
    text.append(getButton(('Your Score: ' + str(player.score)), 'tiny', BLACK, X, Y, None))
    Y += 25
    text.append(getButton(('Number of black squares collected: ' + str(player.numCollisions)), 'tiny', BLACK, X, Y, None))
    Y += 25
    text.append(getButton(('Square collection score: ' + str(player.rectScore) + ' , Time bonus: ' + str(player.timeScore)), 'tiny', BLACK, X, Y, None))
    #\/\/\/\/\/\/\/\/\/\/\ the actual displaying of the message
    pygame.event.pump()
    pygame.event.clear()
    loop = 0
    endMessage = True
    while endMessage:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()
        Screen.fill(WHITE)
        for t in text:
            t.blit(Screen)
        pygame.draw.line(Screen, BLACK, (tempX1,tempY), (tempX2,tempY), 1)
        pygame.draw.rect(Screen, GREY, pointerRect, 0)
        pygame.display.update()
        
        for event in pygame.event.get(MOUSEBUTTONUP):
            XY = getMousePos()
            for t in text:
                if t.textRect.collidepoint(XY[0], XY[1]):
                    if t.command == 'menu':
                        endMessage = False
        loop += 1
        if loop % 25 == 0:
            pygame.event.pump()
            pygame.event.clear()
    returnHighscores(highscores, player)

def optionsMenuText(player):
    X = int(WINDOWWIDTH/2)
    Y = 15
    text = []
    text.append(getButton('Options', 'basic', BLACK, X, Y, None))#basic, title, small, tiny
    Y += 85
    text.append(getButton('Fullscreen mode: ' + str(player.fullScreen), 'small', GREY, X, Y, 'full'))
    Y += 35
    text.append(getButton('Mouse square size:', 'small', GREY, X, Y, None))
    tempX = text[2].textRect.width/2 + 40
    text.append(getButton(str(player.Rect.rect.width) + ' +', 'small', GREY, (X + tempX), Y, 'mouse'))
    Y += 35
    text.append(getButton('Reset Player Stats', 'small', GREY, X, Y, 'R player'))
    Y += 45
    text.append(getButton('Highscores', 'small', BLACK, X, Y, None))
    Y += 45
    player.gameMode = 'normal'
    highscores = getHighscores(player)
    highscores.sort(reverse = True)
    tempX = WINDOWWIDTH/4
    tempY = Y
    text.append(getButton('Normal', 'small', GREY, tempX, tempY, None))
    tempY += 30
    for i in range(len(highscores)):
        text.append(getButton(str(highscores[i]), 'small', GREY, tempX, tempY, None))
        tempY += 35
    text.append(getButton('reset', 'small', GREY, tempX, tempY, 'reset Nor'))
    player.gameMode = 'psycho'
    highscores = getHighscores(player)
    highscores.sort(reverse = True)
    tempX = (WINDOWWIDTH/2)
    tempY = Y
    text.append(getButton('Psycho', 'small', GREY, tempX, tempY, None))
    tempY += 35
    for i in range(len(highscores)):
        text.append(getButton(str(highscores[i]), 'small', GREY, tempX, tempY, None))
        tempY += 35
    text.append(getButton('reset', 'small', GREY, tempX, tempY, 'reset Psy'))
    player.gameMode = 'powerup'
    highscores = getHighscores(player)
    highscores.sort(reverse = True)
    tempX = (WINDOWWIDTH/4) * 3
    tempY = Y
    text.append(getButton('PowerUps', 'small', GREY, tempX, tempY, None))
    tempY += 35
    for i in range(len(highscores)):
        text.append(getButton(str(highscores[i]), 'small', GREY, tempX, tempY, None))
        tempY += 35
    text.append(getButton('reset', 'small', GREY, tempX, tempY, 'reset Pow'))
    text.append(getButton('Menu', 'title', GREY, X, (WINDOWWIDTH - 65), 'menu'))
    return text
    
def optionsMenu(Screen, player, playerRectSize, playerMaxList):
    text = optionsMenuText(player)

    loop = 0
    optionsMenu = True
    while optionsMenu:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()
        temp = smallFont.render(str(loop), True, BLACK, WHITE)
        Screen.fill(WHITE)
        for t in text:
            t.blit(Screen)
        pygame.display.update()
        
        for event in pygame.event.get(MOUSEBUTTONUP):
            XY = getMousePos()
            for t in text:
                if t.textRect.collidepoint(XY[0], XY[1]):
                    if t.command == 'menu':#exit to menu
                        optionsMenu = False
                    elif t.command == 'full':#fullscreen toggle
                        if player.fullScreen == False:
                            Screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), FULLSCREEN)
                        elif player.fullScreen == True:
                            Screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
                        player.fullScreen = not(player.fullScreen)
                    elif t.command == 'mouse':#the mouse square size 
                        currRectWidth = player.Rect.rect.width
                        if currRectWidth < 32:
                            player.Rect = newRect(currRectWidth + 1, BLACK, player)
                        else: player.Rect = newRect(8, BLACK, player)
                    elif t.command == 'R player':
                        player.__init__(playerRectSize, playerMaxList, 'normal')#reset all of the stats using the initialise values
                    elif t.command == 'reset Nor':
                        player.gameMode = 'normal'
                        highscores = [0,0,0,0,0]
                        returnHighscores(highscores, player)
                    elif t.command == 'reset Psy':
                        player.gameMode = 'psycho'
                        highscores = [0,0,0,0,0]
                        returnHighscores(highscores, player)
                    elif t.command == 'reset Pow':
                        player.gameMode = 'powerup'
                        highscores = [0,0,0,0,0]
                        returnHighscores(highscores, player)


        text = optionsMenuText(player)#as things are clicked on by the user the text must update to show the changes
        loop += 1
        if loop % 25 == 0:
            pygame.event.pump()
            pygame.event.clear()
    return Screen, player

def getMousePos():
    x,y = pygame.mouse.get_pos()
    return [x, y]

def updateScreen(Screen, RectList, player, scoreList):
    if player.invincible == True:
        score, scoreRect = textCreator(str(player.score), 'basic', RED)
    else: score, scoreRect = textCreator(str(player.score), 'basic', GREY)
    if player.clock.sec < 10:
        sec = '0' + str(player.clock.sec)
    else: sec = str(player.clock.sec)
    if player.invincible == True:
        gameTime, gameTimeRect = textCreator((str(player.clock.min) + ':' + sec), 'small', RED)#when invincible it makes the timer go red
    else: gameTime, gameTimeRect = textCreator((str(player.clock.min) + ':' + sec), 'small', GREY)
    if player.gameMode == 'psycho':
        backColour = random.choice([PALEBLUE, PINK, LIGHTBROWN, WHITE])
    else: backColour = WHITE

    backSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT)).convert_alpha()
    backSurf.fill(backColour)
    backSurf.blit(score, ((WINDOWWIDTH/2 - scoreRect.width/2),(WINDOWHEIGHT/2 - scoreRect.height/2)))
    backSurf.blit(gameTime,(0,0))

    for R in RectList:
        if R.type == 'good' and R.powerup != None:
            pygame.draw.ellipse(backSurf, R.colour, R.rect)
        else: pygame.draw.rect(backSurf, R.colour, R.rect)
    for R in RectList:
        if R.type == 'bad':#if the square is a bad one
            if player.gameMode == 'psycho':
                R.colour = random.choice([RED, YELLOW, GREEN, BLUE, PURPLE, ORANGE, BROWN])
            pygame.draw.rect(backSurf, R.colour, R.rect)
    pygame.draw.rect(backSurf, player.Rect.colour, player.Rect.rect)
    for S in scoreList:
        backSurf.blit(S.text, (S.xCoord, S.yCoord))
        
    Screen.blit(backSurf, (0,0))
    pygame.display.update()

def GameLoop(Clock, player):
    RectList = []
    scoreList = []
    loop = 0
    GameInPlay = True
    while GameInPlay:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()
            
        if len(RectList) < player.list_max_len:
            colour = random.choice([RED, BLACK])
            size = random.choice(['small', 'large'])
            RectList.append(newRect(size, colour, player))
        
        ms = Clock.tick()
        player.updateClock(ms)
        for S in scoreList[:]:
            S.timeLeft -= ms
            S.fadeColour()#fades the colour of the text so that it disappears gradually
            if S.timeLeft <= 0:
                scoreList.remove(S)

        for R in RectList[:]:#the [:] means it iterates through a copy of the list enabling me to remove items while passing over the list
            R.updatePos(RectList, player.ScreenRect)
        player.updateMousePos()
        for R in RectList[:]:
            if (R.rect.colliderect(player.Rect.rect)):
                if R.type == 'bad' and player.invincible == False:
                    GameInPlay = False
                elif R.type == 'good':
                    if R.powerup == None:
                        score = (40 - R.rect.width)#the 40 is the max rect size add 8
                        score += 5#automatic 5 bonus points and each rect has its own size so that is the point system
                        player.score += score
                        player.rectScore += score
                        player.numCollisions += 1
                        RectList.remove(R)
                        player.sleep -= player.clock.sleep_rect
                        scoreList.append(scoreText(R.xCoord, R.yCoord, score, 1500))#1500 milliseconds which is 1 second
                    elif R.powerup == 'speed':
                        player.sleep += (player.clock.sleep_rect * 100)#the opposite effect of hitting 100 squares so the game slows down
                        RectList.remove(R)
                        scoreList.append(scoreText(R.xCoord, R.yCoord, 'speed', 1500))#1000 milliseconds which is 1 second
                        player.currPower = False
                    elif R.powerup == 'points':
                        player.score += 500#500 increase in the players score
                        RectList.remove(R)
                        scoreList.append(scoreText(R.xCoord, R.yCoord, 500, 1500))#1000 milliseconds which is 1 second
                        player.currPower = False
                    elif R.powerup == 'invincibility':
                        player.invincible = True
                        player.invincible_timer = 5000#5000 milliseconds or 5 seconds
                        RectList.remove(R)
                        scoreList.append(scoreText(R.xCoord, R.yCoord, 'invincibility', 1500))#1000 milliseconds which is 1 second
                    
        updateScreen(Screen, RectList, player, scoreList)
        loop += 1
        if loop % 25 == 0:
            pygame.event.pump()
            pygame.event.clear()
        time.sleep(player.sleep)
    displayEndGame(player)

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ END OF FUNCTIONS - START OF RUNNING GAME CODE

X = int(WINDOWWIDTH/2)
Y = int(WINDOWHEIGHT/8)
menuButtons.append(getButton('Block Dodger!', 'title', BLACK, X, Y, None))
Y += 85
menuButtons.append(getButton('Start Game', 'small', GREY, X, Y, 'start'))
Y += 50
menuButtons.append(getButton('Options', 'small', GREY, X, Y, 'options'))
Y += 50
menuButtons.append(getButton('Quit', 'small', GREY, X, Y, 'quit'))
Y += 100
menuButtons.append(getButton('Start Psycho Game', 'small', GREY, X, Y, 'startPsycho'))
Y += 50
menuButtons.append(getButton('Start PowerUps Game', 'small', GREY, X, Y, 'startPowerUp'))

menuLoop = 0
player = newPlayer(playerRectSize, playerMaxList, 'normal')
while True:
    for event in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()
    Screen.fill(WHITE)
    for mB in menuButtons:
        mB.blit(Screen)
    pygame.display.update()

    for event in pygame.event.get(MOUSEBUTTONUP):
        XY = getMousePos()
        for mB in menuButtons:
            if mB.textRect.collidepoint(XY[0], XY[1]):
                if mB.command == 'start':
                    player.resetScores('normal')#'normal'
                    GameLoop(Clock, player)
                elif mB.command == 'options':
                    Screen, player = optionsMenu(Screen, player, playerRectSize, playerMaxList)
                elif mB.command == 'quit':
                    pygame.quit()
                    sys.exit()
                elif mB.command == 'startPsycho':
                    player.resetScores('psycho')#'psycho'
                    GameLoop(Clock, player)
                elif mB.command == 'startPowerUp':
                    player.resetScores('powerup')#'powerup'
                    GameLoop(Clock, player)
    menuLoop += 1
    if menuLoop % 25 == 0:
        pygame.event.pump()
        pygame.event.clear()
