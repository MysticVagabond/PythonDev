#CREATED BY STEPHEN FISHER
import time, random, sys
ship1Score = 3
ship2Score = 3
ship3Score = 3
ship4Score = 3
shotsTaken = 0
misses = 0
missesTally = 0
lives = 3
Alphabet = 'A B C D E F G H I J'.split()
row1 = [' ~ '] * 10
row2 = [' ~ '] * 10
row3 = [' ~ '] * 10
row4 = [' ~ '] * 10
row5 = [' ~ '] * 10
row6 = [' ~ '] * 10
row7 = [' ~ '] * 10
row8 = [' ~ '] * 10
row9 = [' ~ '] * 10
row10 = [' ~ '] * 10
columns = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]#creates the grid places
columns[0][5] = ' S '#these are the coordinates of your sub
columns[1][5] = ' S '
columns[2][5] = ' S '
ship1 = []
ship2 = []
ship3 = []
ship4 = []
SHIPS = [ship1, ship2, ship3, ship4]
def welcome():#very obvious
    print('Welcome to my Battleships game')
    print('To see instructions type "help"')#asks if you want help
    print('Continue?')
def Help():#gives a background story and the rules of the game
    print('If this is your first time playing Battleships then here are the rules.')
    print()
    print('The story goes...')
    time.sleep(2)
    print('You are the slightly mad captain of a submarine...')
    time.sleep(2)
    print()
    print('On your travels you stumble across some enemy')
    time.sleep(1)
    print('ships and are ordered to destroy them all by your HQ...')
    time.sleep(1)
    print('You are preparing the first shot when')
    time.sleep(1)
    print('suddenly the sub violently shakes and you')
    time.sleep(1)
    print('hear a gigantic explosion at the back of the sub.')
    print()
    time.sleep(1)
    print('To do this you must obey the rules:')
    print('--"~" represents the water')
    print('--"S" represents your submarine, which you CANNOT hit')
    print('--Your Sonar has been destroyed so you will have to fire randomly')
    print('--If you get a Hit the "~" will be replaced by an "X"')
    print('-- If you however Miss the "~" will be replaced by an "O"')
    print('--To select a specific grid square, type first the ')
    print('   x-coodinate and then the y-coordinate(CAPS LOCK is good)')
    print('--There are 4 ships for you to destroy in this game')
    print('--There is a twist though every 3 misses without a hit the enemies')
    print('      get lucky; hit you and you lose a life,')
    print("--3 lives and you're sunk - Game Over")
    print()
    input('Continue?')
    print()
    print()
def grid():#prints the grid 
    global columns
    global rows
    global Aplhabet
    width = len(columns)
    height = len(columns)
    n = 0
    n1 = 0
    print('Y')
    for z in range(0,height):#prints each set of lines *rows of the grid
        print('  ', end = '')
        for x in range(0,width):#prints the top line of each grid square
            print('+---', end = '')
        print('+')
        letter = Alphabet[n]
        print(letter, '|', end = '')#prints the coordinate on the side axis and the border
        n +=1
        for i in range(0,width):#prints the values in the lists in the correct places
            print(columns[z][i], end = '|')
        print()
    print('  ', end = '')
    for x in range(0,width):#prints the last line of the grid squares
        print('+---', end = '')
    print('+')
    print('  ', end = '')
    for x in range(0,width):#finally prints the coordinates on the bottom axis
        print(end = ' ')
        print('', n1, '', end = '')
        n1 += 1
    print('  X')
    print()
def coordinates():#asks for your input for x and y and checks its a number and between 0,9
    global xcoor
    global ycoor
    foundX = False
    foundY = False
    Xwrong = False
    Ywrong = False
    foundXY = False
    while foundXY == False:
        rawCoor = input('Coorinates?(xy)')
        if len(rawCoor) == 2:
            rawList = list(rawCoor)
            xcoor = rawList[0]
            ycoord = rawList[1]
            foundRaw = True
        else:
            print('Try Again!')
        if xcoor.isdigit():
            if 0 <= int(xcoor) <= 9:
                xcoor = int(xcoor)
                foundX = True
            else:
                print('Try Again! - X is wrong')
                Xwrong = True
        else:
            print('Try Again! - X is wrong')
            Xwrong = True
        ycoord = ycoord.upper()
        if ycoord in Alphabet:
            ycoor = Alphabet.index(ycoord)
            foundY = True
        else:
            print('Try Again! - Y is wrong')
            Ywrong = True
        if Xwrong == True and Ywrong == True:
            print()
            print('X coordinate first\nthen the Y coordinate!')
            print()
        if foundX == True and foundY == True:
            foundXY = True
    print()
def shipPosition():
    global SHIPS
    for s in range(0,4):
        rotation = random.randint(0,1)
        rotation = str(rotation)
        if s == 0:
            if (rotation == '0'):
                shipPlace = random.randint(1,3)
                shipPlace1 = random.randint(0,4)
            elif (rotation == '1'):
                shipPlace = random.randint(0,4)
                shipPlace1 = random.randint(1,3)
        elif s == 1:
            if (rotation == '0'):
                shipPlace = random.randint(7,8)
                shipPlace1 = random.randint(0,4)
            elif (rotation == '1'):
                shipPlace = random.randint(6,9)
                shipPlace1 = random.randint(1,3)
        elif s == 2:
            if (rotation == '0'):
                shipPlace = random.randint(1,3)
                shipPlace1 = random.randint(5,9)
            elif (rotation == '1'):
                shipPlace = random.randint(0,5)
                shipPlace1 = random.randint(6,8)
        elif s == 3:
            if (rotation == '0'):
                shipPlace = random.randint(6,8)
                shipPlace1 = random.randint(6,9)
            elif (rotation == '1'):
                shipPlace = random.randint(5,9)
                shipPlace1 = random.randint(6,8)
        if (rotation == '0'):
            x1 = shipPlace + 1
            x2 = shipPlace
            x3 = shipPlace - 1
            y = shipPlace1
            place1 = (str(x1) + '.' + str(y))
            place2 = (str(x2) + '.' + str(y))
            place3 = (str(x3) + '.' + str(y))
        elif (rotation == '1'):
            x = shipPlace
            y1 = shipPlace1 + 1
            y2 = shipPlace1
            y3 = shipPlace1 - 1
            place1 = (str(x) + '.' + str(y1))
            place2 = (str(x) + '.' + str(y2))
            place3 = (str(x) + '.' + str(y3))
        else:
            print('ERROR')
        SHIPS[s].append(place1)
        SHIPS[s].append(place2)
        SHIPS[s].append(place3)
    print()
def gamePlay():#the main section of the game
    global xcoor
    global ycoor
    global ship1Score
    global ship2Score
    global ship3Score
    global ship4Score
    global foundShips
    global shotsTaken
    global misses
    global lives
    global missesTally
    global ship1
    global ship2
    global ship3
    global ship4
    sunkShip1 = False
    sunkShip2 = False
    sunkShip3 = False
    sunkShip4 = False
    sunkAll = False
    shipsSunkTally = 0#up to here is the variables and lists
    yourSub = ['5.0', '5.1', '5.2']
    attemptList = []
    while sunkAll == False:
        attempt = str(xcoor) + '.' + str(ycoor)
        if attempt in SHIPS[0]:
            print('HIT!')
            columns[int(ycoor)][int(xcoor)] = ' X '#checks if your input is in one of the ships positions
            ship1Score -= 1
            shotsTaken += 1
            misses = 0
            attemptList.append(attempt)
            if ship1Score == 0:
                print('SHIP SUNK! Well Done!')
                shipsSunkTally += 1
                sunkShip1 = True
        elif attempt in SHIPS[1]:
            print('HIT!')
            columns[int(ycoor)][int(xcoor)] = ' X '
            ship2Score -= 1
            shotsTaken += 1
            misses = 0
            attemptList.append(attempt)
            if ship2Score == 0:
                print('SHIP SUNK! Well Done!')
                shipsSunkTally += 1
                sunkShip2 = True
        elif attempt in SHIPS[2]:
            print('HIT!')
            columns[int(ycoor)][int(xcoor)] = ' X '
            ship3Score -= 1
            shotsTaken += 1
            misses = 0
            attemptList.append(attempt)
            if ship3Score == 0:
                print('SHIP SUNK! Well Done!')
                shipsSunkTally += 1
                sunkShip3 = True
        elif attempt in SHIPS[3]:
            print('HIT!')
            columns[int(ycoor)][int(xcoor)] = ' X '
            ship4Score -= 1
            shotsTaken += 1
            misses = 0
            attemptList.append(attempt)
            if ship4Score == 0:
                print('SHIP SUNK! Well Done!')
                shipsSunkTally += 1
                sunkShip4 = True
        elif attempt in yourSub:
            print('You CANNOT hit yourself,\nTry Again!')
        elif attempt in attemptList:
            print('You have already shot there!\nTry Again!')
        else:
            print('You missed, Try Again!')
            columns[int(ycoor)][int(xcoor)] = ' O '
            misses  = int(misses)
            misses += 1
            shotsTaken += 1
            missesTally += 1
            attemptList.append(attempt)
        if (str(misses) == '3'):#if not you get a hit after 3 misses you lose a life
            lives -= 1
            misses = 0
            print('Lives left:', lives)#counts down your lives
        if (str(lives) == '0'):
            print('You died. Game Over!')
            time.sleep(2)
            gameOver()
            break
        if sunkShip1 == True and\
        sunkShip2 == True and\
        sunkShip3 == True and\
        sunkShip4 == True:#checks the number of ships sunk
            foundShips = True
            print('Yes! You have sunk all of the ship(s)')
            time.sleep(2)
            gameWon()
            break
        elif shipsSunkTally != 0:print('Well done you have sunk:', shipsSunkTally, 'ships')
        elif shipsSunkTally == 0:print('You have not yet managed to sink a ship!')
        grid()
        coordinates()
def gameWon(): #ends the game when it is won
    global missesTally
    global shotsTaken
    print('YES! You have completed the task set and destroyed all 4 ships!!')
    print('You required:', shotsTaken , 'hits and:', missesTally, 'misses to destroy the ships!')
    print('YOU WON')
def gameOver():#ends the game when it is lost
    global foundShips
    print('You got hit 3 times and were blown to pieces...')
    print('You have FAILED')
    foundShips = True
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    welcome()
    if(input() == 'help' or input() == 'HELP' or input() == 'Help'):
        Help()
    foundShips = False#makes sure that the game ends when ships are destroyed
    while foundShips == False:
        shipPosition()
        grid()
        coordinates()#calls the 3 def blocks required to play
        gamePlay()
    playAgain = input('Do you want to play again (no\yes)?')#asks to play again
    if playAgain == 'yes' or playAgain == 'y':
        playAgain = 'yes'
    else:
        playAgain = 'no'
sys.exit()
