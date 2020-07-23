import time, sys
player1Char = ''
player2Char = ''
xcoor = ''
ycoor = ''
turnChar = ''
Winner = ''
turn = 1
goes = 0
gameOver = False
winnerFound = False
SMILEY = ['''
____________________
___@@@@______@@@@___
__@@@@@@____@@@@@@__
__@@@@@@____@@@@@@__
___@@@@______@@@@___
_________@@_________
_@@______________@@_
__@@____________@@__
___@@@________@@@___
_____@@@@@@@@@@_____
____________________

''', '''
____________________
___@@@@______@@@@___
__@@@@@@____@@@@@@__
__@@@@@@____@@@@@@__
___@@@@______@@@@___
_________@@_________
____________________
_____@@@@@@@@@@_____
___@@@________@@@___
__@@____________@@__
_@@______________@@_
____________________
''']
def welcome():#very obvious
    print('Welcome to my Connnect 4 game')
    print('To see instructions type "help"')#asks if you want help
    print('Continue?')
def Help():#gives a background story and the rules of the game
    print('If this is your first time playing Connect 4 then here are the rules.')
    print()
    print('1. Choose who plays first')
    time.sleep(1.5)
    print('2. Each player in his turn chooses one of the spaces in the top of the grid to place the counter')
    time.sleep(1.5)
    print('3. The play alternates until one of the players gets four counters of his type in a row')
    time.sleep(1.5)
    print('4. The four in a row can be horizontal, vertical, or diagonal')
    time.sleep(1.5)
    print('5. The first player to get four in a row wins')
    time.sleep(1.5)
    print('6. If the board is filled with pieces and neither player has 4 in a row, then the game is a draw')
    print()
def playerOptions():
    global player1Char
    global player2Char
    P1 = False
    P2 = False
    while P1 == False:
        print('Player 1 pick a character')
        IN = input()
        if len(IN) == 1:
            player1Char = ' ' + str(IN) + ' '
            P1 = True
        else:
            print('Try Again?(y/n)')
            if input().lower() == 'y':
                P1 = False
            else:
                P1 = True
                player1Char = ' X '
    while P2 == False:
        print('Player 2 pick a character')
        IN = input()
        if len(IN) < 2:
            player2Char = ' ' + str(IN) + ' '
            P2 = True
        else:
            print('Try Again?(y/n)')
            if input().lower() == 'y':
                P2 = False
            else:
                P2 = True
                player2Char = ' O '
def createGrid():
    global columns
    row1 = ['   '] * 7
    row2 = ['   '] * 7
    row3 = ['   '] * 7
    row4 = ['   '] * 7
    row5 = ['   '] * 7
    row6 = ['   '] * 7
    columns = [row1, row2, row3, row4, row5, row6]
def grid():
    global columns
    width = len(columns) + 1
    height = len(columns)
    n = 0
    n1 = 0
    for z in range(0,height):#prints each set of lines *rows* of the grid
        print('  ', end = '')
        for x in range(0,width):#prints the top line of each grid square
            print('+---', end = '')
        print('+')
        print(' ', '|', end = '')#prints the coordinate on the side axis and the border
        n += 1
        for i in range(0,width):#prints the values in the lists in the correct places
            print(columns[z][i], end = '|')
        print()
    print('  ', end = '')
    for x in range(0,width):#prints the last line of the grid squares
        print('+---', end = '')
    print('+')
    print('  ', end = '')
    for x in range(0,width):#finally prints the coordinates on the bottom axis
        print(' ', n1, '',  end = '')
        n1 += 1
    print()
def turnChecker():#checks whos turn it is currently
    global xcoor
    global ycoor
    global player1Char
    global player2Char
    global turn
    global turnChar
    if (str(turn) == '1'):
        turn += 1
        print("Player 1's turn")
        print('You are the:', player1Char)
        turnChar = player1Char
    elif (str(turn) == '2'):
        turn -= 1
        print("Player 2's turn")
        print('You are the:', player2Char)
        turnChar = player2Char
    else:
        print('Fails')
def coordinates():#asks for your input for x and y and checks its a number and between 0,9
    global xcoor
    global goes
    foundX = False
    while foundX == False:
        print('Position? (X Coordinate),\n-type "quit" to exit the game')
        xcoor = input()
        if xcoor.isdigit():
            if 0 <= int(xcoor) <= 6:
                foundX = True
                goes += 1
            else:
                print('Try Again!\n-Too high')
        elif xcoor.lower() == 'quit':
            sys.exit()
        else:
            print('Try Again!\n-Not a number')
def yCoordChecker():
    global ycoor
    global xcoor
    global player1Char
    global player2Char
    global turnChar
    nCheck = 5
    foundY = False
    xcoor = int(xcoor)
    while foundY == False:
        for i in range(0,7):
            if (str(xcoor) == str(i)):
                if nCheck < 0:
                    print('There is no available space here!')
                    print()
                    return coordinates()
                else:
                    if columns[nCheck][xcoor] != player1Char:
                        if columns[nCheck][xcoor] != player2Char:
                            ycoor = int(nCheck)
                            foundY = True
                        else:
                            nCheck -= 1
                            ycoor = ''
                    else:
                        nCheck -= 1
                        ycoor = ''
        if ycoor == '':
            ycoor = ycoor
        else:
            if 0 <= int(ycoor) <= 6:
                columns[ycoor][xcoor] = turnChar
            else:
                print('Fails')
def gameWinCheck():
    global columns
    global turnChar
    global winnerFound
    global goes
    #gr = grid and tu = turnChar
    c = columns
    t = turnChar
    for x in range(0,4):
        for y in range(0,6): #all horizontal ones
            if((c[y][x] == t) and (c[y][x+1] == t) and (c[y][x+2] == t) and (c[y][x+3] == t)):
                winnerFound = True
    for x in range(0,6):
        for y in range(0,3):#all vertical ones
            if((c[y][x] == t and c[y+1][x] == t and c[y+2][x] == t and c[y+3][x] == t)):
                winnerFound = True
    for x in range(0,4):#diagonally up from left to right
        for y in range(0,3):
            n = 5 - y
            if((c[n][x] == t and c[n-1][x+1] == t and c[n-2][x+2] == t and c[n-3][x+3] == t)):
                winnerFound = True
    for x in range(0,3):#diagonally up from right to left
        n1 = 5 - x
        for y in range(0,4):
            n = 6 - y
            if((c[n1][n] == t and c[n1-1][n-1] == t and c[n1-2][n-2] == t and c[n1-3][n-3] == t)):
                winnerFound = True
    if goes == 42:
        winnerFound = 'Draw'
def gameEnd(): #ends the game when it is won
    global player1Char
    global player2Char
    global turnChar
    global gameOver
    global winnerFound
    if winnerFound == True:
        grid()
        if turnChar == player1Char:
            Winner = 'Player 1'
            gameOver = True
            print('Well Done Player 1, you have won the game!')
        elif turnChar == player2Char:
            Winner = 'Player 2'
            gameOver = True
            print('Well Done Player 2, you have won the game!')
        else:
            print('Win fails')
        print(SMILEY[0])
        
    if winnerFound == 'Draw':
        print('The Game is a DRAW, You both FAILED!')
        print(SMILEY[1])
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    welcome()
    HelpInput = input()
    if((HelpInput == 'help') or (HelpInput == 'HELP') or (HelpInput == 'Help')):
        Help()
    playerOptions()
    createGrid()
    while gameOver == False:
        grid()
        turnChecker() 
        coordinates()
        yCoordChecker()
        gameWinCheck()
        gameEnd()
    playAgain = input('Do you want to play again (no\yes)?')#asks to play again
    if playAgain == 'yes' or playAgain == 'y':
        gameOver = False
        print()
    else:
        print()
