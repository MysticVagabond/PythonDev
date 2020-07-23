#Stephen Fisher 15/02/12

import random, sys, pygame, time
from pygame.locals import *
pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 420
GRIDWIDTH = 40
GRIDHEIGHT = 40
Screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

BLACK = (0, 0, 0)#set up colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (100, 100, 100)

clock = pygame.time.Clock()
pygame.event.pump()

LEFT = 9#uses same value as the clock face for simplicity - doesnt matter what its just for the user
RIGHT = 3
UP = 12
DOWN = 6

basicFont = pygame.font.SysFont(None, 25)#set up fonts
menuFont = pygame.font.SysFont(None, 50)

snakePart = {'rect':pygame.Rect(0, 0, 10, 10), 'colour': WHITE}

def resetVariables():
    global direction, score, foodEatenNum, speed, addSnakePart
    direction = LEFT
    score = 0
    speed = 7
    addSnakePart = False

def newGrid():
    global grid,snakeList, foodList
    grid = []
    snakeList = []
    foodList = []
    for i in range(GRIDHEIGHT):
        grid.append([' '] * GRIDWIDTH)
    grid[20][20] = 's'#starting pos for snake
    grid[20][21] = 's'
    grid[20][22] = 's'
    grid[20][23] = 's'
    grid[20][24] = 's'
    snakeList.append([20, 20])
    snakeList.append([20, 21])
    snakeList.append([20, 22])
    snakeList.append([20, 23])
    snakeList.append([20, 24])

    x = randomNum(5,35)
    y = randomNum(5,35)
    grid[x][y] = 'f'#first and only food
    foodList.append([x, y])
    
def blankOutGrid(grid):
    for x in range(GRIDHEIGHT):
        for y in range(GRIDWIDTH):
            grid[x][y] = ' '
    return grid

def getMousePos():
    x,y = pygame.mouse.get_pos()
    return [x, y]

def createText(score, speed):
    global coordText, coordTextRect, scoreText, scoreTextRect, pause, pauseRect, quitText, quitTextRect, speedText
    
    XY = getMousePos()
    coordText = basicFont.render(str(XY[0]) + ',' + str(XY[1]), True, WHITE, BLACK)
    coordTextRect = coordText.get_rect()
    scoreText = basicFont.render('Score:' + str(score), True, WHITE)
    scoreTextRect = scoreText.get_rect()
    pause = basicFont.render('Pause   ', True, WHITE)
    pauseRect = pause.get_rect()
    quitText = menuFont.render('Quit', True, WHITE, BLACK)
    quitTextRect = quitText.get_rect()
    speedText = basicFont.render('Speed:' + str(speed), True, WHITE, BLACK)
    
def addFood(score, loopNum):
    global foodList, speed, addSnakePart
    
    food = len(foodList)
    if food == 0 and score <= 1200:
        foodList.append([randomNum(2,37), randomNum(2,37)])
        addSnakePart = True
        
    elif score >= 1300 and food == 0:
        foodList.append([randomNum(0,39), randomNum(0,39)])
        foodList.append([randomNum(0,39), randomNum(0,39)])
        addSnakePart = True
    elif (loopNum % 100) == 0 and food == 0:
        foodList.append([randomNum(0,39), randomNum(0,39)])
        foodList.append([randomNum(0,39), randomNum(0,39)])
        addSnakePart = True
        
    for x,y in foodList:
        grid[x][y] = 'f'
        
def foodEaten(xNew, yNew, direction):
    global snakeList, foodList, score, speed
    
    if grid[xNew][yNew] == 'f':
        score += 100
        foodList.remove([xNew, yNew])
        if score <= 1200:
            speed += .5
        elif score >= 1300:
            speed += 1
        
def randomNum(a,b):
    return random.randint(a,b)
    
def saveScore(score):
    global scoreList
    try:
        scoreList = []
        file = open('Project Files\Snakes\Snakes HighScores.txt', 'r')
        for line in file:
            scoreList.append(int(line))
    except IOError:
        scoreList = [0,0,0,0,0,0,0,0,0,0]
        
    scoreList.append(int(score))
    scoreList.sort()
    
    while len(scoreList) > 10:
        scoreList.remove(scoreList[0])
    file = open('Project Files\Snakes\Snakes HighScores.txt', 'w')
    for i in scoreList:
        file.write(str(i) + '\n')
        
def collideCheck(xNew, yNew, direction):
    global snakeList
    
    if -1 >= xNew or 40 <= xNew or -1 >= yNew or 40 <= yNew:
        return False
    for x,y in snakeList:
        if x == xNew and y == yNew:#for every body part it checks if the snake head has hit it
            return False
    return True

def directionCheck(direction):
    global grid
    global snakePart
    
    for event in pygame.event.get(QUIT):
            terminate()
    screenUpdate(grid, snakePart)
    
    for event in pygame.event.get(KEYDOWN):#checks if direction has changed before moving the snake
        if (event.key == K_w or event.key == K_UP) and direction != DOWN:
            direction = UP
        elif (event.key == K_a or event.key == K_LEFT) and direction != RIGHT:
            direction = LEFT
        elif (event.key == K_s or event.key == K_DOWN) and direction != UP:
            direction = DOWN
        elif (event.key == K_d or event.key == K_RIGHT) and direction != LEFT:
            direction = RIGHT
    screenUpdate(grid, snakePart)
    
    for event in pygame.event.get(QUIT):
            terminate()
    return direction
    
def snakeMove(grid):
    global snakeList, addSnakePart, playAgain
    
    for i in range(0, len(snakeList)):
        for event in pygame.event.get(QUIT):
            terminate()
            
        x = snakeList[i][0]
        y = snakeList[i][1]
        if i == 0:
            xPrev = x
            yPrev = y
            if direction == LEFT:
                xNew = x
                yNew = y-1             
            elif direction == RIGHT:
                xNew = x
                yNew = y+1 
            elif direction == UP:
                xNew = x-1
                yNew = y
            elif direction == DOWN:
                xNew = x+1
                yNew = y
            if not collideCheck(xNew, yNew, direction):
                playAgain = gameOverLoop()
                resetVariables()
                break
            else:
                foodEaten(xNew, yNew, direction)
                snakeList[i] = [xNew, yNew]
                grid[snakeList[i][0]][snakeList[i][1]] = 's'
        else:
            snakeList[i] = [xPrev, yPrev]
            xPrev = x
            yPrev = y
            grid[snakeList[i][0]][snakeList[i][1]] = 's'
    if addSnakePart == True:
        snakeList.append([xPrev, yPrev])
        addSnakePart = False
    
def gameOverLoop():
    global Screen, coordTextRect, quitTextRect, playAgain
    pygame.event.clear()
    
    dead = menuFont.render('You Crashed!', True, WHITE)
    gameOver = menuFont.render('GAME OVER', True, WHITE)
    retry = menuFont.render('Retry', True, WHITE)
    retryRect = retry.get_rect()

    saveScore(score)
    
    Screen.fill(BLACK)
    Screen.blit(gameOver, (90, 90))
    Screen.blit(dead, (85, 40))
    Screen.blit(retry, (50, 350))
    Screen.blit(quitText, (200, 350))
    Screen.blit(coordText, (0,0))
    Screen.blit(scoreText, (0 + coordTextRect.width + 20, 0))
    pygame.draw.line(Screen, WHITE, (0, 19), (WINDOWWIDTH, 19))
    y = 130#starts off at a height of 130 and adds 18 before printing the next score
    for i in range(0, len(scoreList)):
        try:
            num = len(scoreList) - i
            scorePrint = basicFont.render(str(num) + '.  ' + str(scoreList[i]), True, WHITE)
            Screen.blit(scorePrint, (120, y))
        except IndexError:
            scorePrint = basicFont.render(str(num) + '.  ' + '0', True, WHITE)
            Screen.blit(scorePrint, (120, y))
        y += 18
    pygame.display.update()
    
    while True:
        for event in pygame.event.get(QUIT):
            terminate()
        XY = getMousePos()
        for event in pygame.event.get(MOUSEBUTTONUP):#clicking the retry button
            if (50 <= XY[0] <= (retryRect.width + 50)) and (350 <= XY[1] <= (retryRect.height + 350)):
                pygame.display.update()
                Screen.fill(BLACK)
                Screen.blit(coordText, (0,0))
                newGrid()
                resetVariables()
                return True
                            #clicking the quit button
            elif (200 <= XY[0] <= (quitTextRect.width + 200)) and (350 <= XY[1] <= (quitTextRect.height + 350)):
                pygame.display.update()
                terminate()
    
def helpLoop():
    back = menuFont.render('Back', True, WHITE)
    backRect = back.get_rect()
    inst1 = menuFont.render('Instructions', True, WHITE)
    inst1Rect = inst1.get_rect()
    inst2 = basicFont.render('Using the arrow keys or WASD keys move ', True, WHITE)
    inst2Rect = inst2.get_rect()
    inst3 = basicFont.render('the snake round the screen.The aim is to ', True, WHITE)
    inst3Rect = inst3.get_rect()
    inst4 = basicFont.render('collect the red apples which appear ', True, WHITE)
    inst4Rect = inst4.get_rect()
    inst5 = basicFont.render('around the screen at random times. The', True, WHITE)
    inst5Rect = inst5.get_rect()
    inst6 = basicFont.render('snake will get longer and faster so be ', True, WHITE)
    inst6Rect = inst6.get_rect()
    inst7 = basicFont.render('careful not to run into the walls or ', True, WHITE)
    inst7Rect = inst7.get_rect()
    inst8 = basicFont.render('yourself as in both cases you die,', True, WHITE)
    inst8Rect = inst8.get_rect()
    inst9 = basicFont.render(' GAME OVER!', True, WHITE)
    inst9Rect = inst9.get_rect()

    Screen.fill(BLACK)
    Screen.blit(back, (150, 330))
    Screen.blit(inst1, (90, 30))#1
    y = inst1Rect.height + 60
    Screen.blit(inst2, (20, y))#2
    y += inst2Rect.height + 10
    Screen.blit(inst3, (20, y))#3
    y += inst3Rect.height + 10
    Screen.blit(inst4, (20, y))#4
    y += inst4Rect.height + 10
    Screen.blit(inst5, (20, y))#5
    y += inst5Rect.height + 10
    Screen.blit(inst6, (20, y))#6
    y += inst6Rect.height + 10
    Screen.blit(inst7, (20, y))#7
    y += inst7Rect.height + 10
    Screen.blit(inst8, (20, y))#8
    y += inst8Rect.height + 10
    Screen.blit(inst9, (120, y))#9
    y += inst9Rect.height + 10
    
    helpOpen = True
    while helpOpen:
        pygame.display.update()
        for event in pygame.event.get(QUIT):
            terminate()
        for event in pygame.event.get(MOUSEBUTTONDOWN):
            XY = getMousePos()
            if (150 <= XY[0] <= backRect.width + 150) and (330 <= XY[1] <= backRect.height + 330):
                helpOpen = False

def optionsLoop(currentColour):
    global snakePart
    pygame.event.clear()
    
    options = menuFont.render('Options', True, WHITE)
    optionsRect = options.get_rect()
    colour = basicFont.render('Colour: ', True, WHITE)
    colourRect = colour.get_rect()
    reset = basicFont.render('Reset Highscores', True, WHITE)
    resetRect = reset.get_rect()
    back = menuFont.render('Back', True, WHITE)
    backRect = back.get_rect()
    
    try:
        file = open('Project Files\Snakes\Snakes HighScores.txt', 'r')
        scoreList = []
        for i in file:
            scoreList.append(int(i))
    except IOError:
        file = open('Project Files\Snakes\Snakes HighScores.txt', 'w')
        scoreList = []
        for i in range(10):
            scoreList.append(int(0))
            
    score = basicFont.render('Current :' + str(scoreList[9]), True, WHITE)
    
    colourList = [WHITE, RED, GREEN, BLUE, YELLOW]
    optionsOpen = True
    colourButtonList = []
    num = colourList.index(currentColour)
    clearLoop = 1
    
    while optionsOpen:
        Screen.fill(BLACK)
        Screen.blit(options, (130, 125))
        Screen.blit(colour, (160 - colourRect.width, 180))
        Screen.blit(reset, (110, 220))#may have to change, change later bits too
        Screen.blit(score, (120, 240))
        Screen.blit(back, (150, 300))
        z = 160
        for i in colourList:
            pygame.draw.rect(Screen, i, (z, 180, 20, 20))
            if clearLoop == 1:
                colourButtonList.append(z)
            z += 24
        coord = colourButtonList[num]
        pygame.draw.rect(Screen, GREY, (coord - 2, 178, 23, 23), 2)

        for event in pygame.event.get(QUIT):
            terminate()
        for event in pygame.event.get(MOUSEBUTTONDOWN):
            XY = getMousePos()
            if (110 <= XY[0] <= resetRect.width + 110) and (220 <= XY[1] <= resetRect.height + 220):
                file = open('Project Files\Snakes\Snakes HighScores.txt', 'w')
                for i in range(10):
                    file.write(str(0) + '\n')
                    scoreList.append(int(i))
                score = basicFont.render('Current :' + str(scoreList[9]), True, WHITE)
            elif (150 <= XY[0] <= backRect.width + 150) and (300 <= XY[1] <= backRect.height + 300):
                snakePart['colour'] = colourList[num]
                optionsOpen = False
            for i in range(5):
                x = colourButtonList[i]
                if (x <= XY[0] <= x + 20) and (180 <= XY[1] <= 200):
                    num = colourButtonList.index(x)
        clearLoop += 1    
        pygame.display.update()
        if clearLoop % 25 == 0:
            pygame.event.clear()
    
def MenuLoop():
    global coordText, snakePart

    playText = menuFont.render('PLAY GAME', True, WHITE, BLACK)
    playTextRect = playText.get_rect()
    options = menuFont.render('Options', True, WHITE, BLACK)
    optionsRect = options.get_rect()
    helpText = menuFont.render('Help', True, WHITE, BLACK)
    helpTextRect = helpText.get_rect()
    
    menuShown = True
    while menuShown:
        for event in pygame.event.get(QUIT):
            terminate()
        createText(0, 0)
        Screen.fill(BLACK)
        Screen.blit(playText, (100, 125))
        Screen.blit(options, (130, 175))
        Screen.blit(helpText, (160, 225))
        Screen.blit(coordText, (0,0))
        pygame.display.update()

        XY = getMousePos()
        for event in pygame.event.get(MOUSEBUTTONUP):#clicking the play button
            if (100 <= XY[0] <= playTextRect.width + 100) and (125 <= XY[1] <= playTextRect.height + 125):
                menuShown = False
            elif (130 <= XY[0] <= optionsRect.width + 130) and (175 <= XY[1] <= optionsRect.height + 175):
                optionsLoop(snakePart['colour'])
                pygame.event.clear()
            elif (160 <= XY[0] <= helpTextRect.width + 160) and (225 <= XY[1] <= helpTextRect.height + 225):
                helpLoop()
                pygame.event.clear()
        pygame.event.pump()
        pygame.event.clear()

def screenUpdate(grid, snakePart):
    global Screen, coordText, coordTextRect, scoreText, scoreTextRect, pause, pauseRect, speedText

    screenRect = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT)).convert_alpha()
    screenRect.fill(BLACK)
    screenRect.blit(coordText, (0,0))
    screenRect.blit(scoreText, (80, 0))#60 for the coord text and 20 for a gap
    screenRect.blit(speedText, (scoreTextRect.width + 100, 0))#20 for a gap
    screenRect.blit(pause, (WINDOWWIDTH - pauseRect.width, 0))
    pygame.draw.line(screenRect, WHITE, (0, 19), (WINDOWWIDTH, 19))
    
    for x in range(GRIDWIDTH):
        for y in range(GRIDHEIGHT):
            if grid[x][y] == 's':
                X = (x * 10) + 20#for the bar at the top
                Y = y * 10
                rect = (Y, X, 10, 10)
                pygame.draw.rect(screenRect, snakePart['colour'], rect)
            elif grid[x][y] == 'f':
                X = (x * 10) + 20#for the bar at the top
                Y = y * 10
                rect = (Y, X, 10, 10)
                pygame.draw.rect(screenRect, RED, rect)

    Screen.blit(screenRect, (0,0))
    pygame.display.update()
    pygame.display.set_caption('Snakes | FPS ' + str(clock.get_fps()))

def terminate():
    pygame.quit()
    sys.exit()

MenuLoop()

showMenu = False
playAgain = True

while playAgain:
    if showMenu == True:
        MenuLoop()
    pygame.event.clear()
    # \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/#starts the game by resetting the variables
    Screen.fill(BLACK)
    Screen.blit(coordText, (0,0))
    newGrid()
    resetVariables()
    # \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/
    gameInPlay = True
    loopNum = 0
    while gameInPlay == True:
        for event in pygame.event.get(QUIT):
            terminate()
        direction = directionCheck(direction)#uses the many def blocks
        createText(score, speed)
        screenUpdate(grid, snakePart)
        grid = blankOutGrid(grid)
        addFood(score, loopNum)
        direction = directionCheck(direction)
        snakeMove(grid)
        screenUpdate(grid, snakePart)
        # \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ #clicking the pause button
        XY = getMousePos()
        for event in pygame.event.get(MOUSEBUTTONUP):
            if (WINDOWWIDTH - pauseRect.width <= XY[0] <= WINDOWWIDTH) and (0 <= XY[1] <= 0 + pauseRect.height):
                
                pauseLarge = menuFont.render('Game Paused', True, WHITE, BLACK)
                resumeText = menuFont.render('Resume', True, WHITE, BLACK)
                resumeTextRect = resumeText.get_rect()
                mainMenuText = menuFont.render('Main Menu', True, WHITE, BLACK)
                mainMenuTextRect = mainMenuText.get_rect()
                Screen.blit(pauseLarge, (90, 75))
                Screen.blit(resumeText, (140, 155))
                Screen.blit(mainMenuText, (110, 200))
                Screen.blit(quitText, (160, 245))
                pygame.display.update()
                paused = True
                
                while paused:
                    for event in pygame.event.get(QUIT):
                        terminate()
                    XY = getMousePos()
                    for event in pygame.event.get(MOUSEBUTTONUP):#pressing the retry button
                        if (140 <= XY[0] <= (resumeTextRect.width + 140)) and (155 <= XY[1] <= (resumeTextRect.height + 155)):
                            paused = False
                    #pressing the main menu button
                        elif (110 <= XY[0] <= (mainMenuTextRect.width + 110)) and (200 <= XY[1] <= (mainMenuTextRect.height + 200)):
                            paused = False
                            showMenu = True
                            gameInPlay = False
                    #pressing the quit button
                        elif (160 <= XY[0] <= (quitTextRect.width + 160)) and (245 <= XY[1] <= (quitTextRect.height + 245)):
                            pygame.display.update()
                            terminate()
                    pygame.event.clear()
        # \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
        clock.tick(speed)
        loopNum += 1
        if loopNum % 25 == 0:
            pygame.event.pump()
            pygame.event.clear()#clears the event list of events of these types
