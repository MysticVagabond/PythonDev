#Authors: Sephenz
import random, sys, time
user = ' P '
userMove = ''
def grid():
    global room1
    global room2
    global room3
    global room4
    global room5
    global room6
    global room7
    global room8
    global room9
    width = 5  #only edit these two numbers to edit grid dimensions
    height = 5  #odd numbers only
    n = (width - 1) / 2
    print()
    for i in range(0,3):
        if i == 0:
            grid1 = room1
            grid2 = room2
            grid3 = room3
        elif i == 1:
            grid1 = room4
            grid2 = room5
            grid3 = room6
        elif i == 2:
            grid1 = room7
            grid2 = room8
            grid3 = room9#sets up each which 2D list to use on each printout
        for z in range(0,height):
            for x in range(0,width):
                    print('+---', end = '')
            print('+', end = '')
            if z == n or z == (n + 1):
                print('---', end = '')
            else:
                print(' W ', end = '')
            for x in range(0,width):
                    print('+---', end = '')
            print('+', end = '')
            if z == n or z == (n + 1):
                print('---', end = '')
            else:
                print(' W ', end = '')
            for x in range(0,width):
                    print('+---', end = '')
            print('+')#up to here is top line of each square
            print('|',end = '')
            for x in range(0,width):
                    print(grid1[z][x], end = '|')
            if z == n:
                print('   ', end = '')
            else:
                print(' W ', end = '')
            print('|',end = '')
            for x in range(0,width):
                    print(grid2[z][x], end = '|')
            if z == n:
                print('   ', end = '')
            else:
                print(' W ', end = '')
            print('|',end = '')
            for x in range(0,width):
                print(grid3[z][x], end = '|')
            print()#to here is the central bit to each square
        for x in range(0,width):
                print('+---', end = '')
        print('+', 'W ', end = '')
        for x in range(0,width):
                print('+---', end = '')
        print('+', 'W ', end = '')
        for x in range(0,width):
                print('+---', end = '')
        print('+')#up to here is the bottom line of each grid
        if i != 2:
            for x in range(0,width):
                if x == n:
                    print('|   ', end = '|')
                else:
                    print('WWWW', end = '')
            print('WW', end = 'W')
            for x in range(0,width):
                if x == n:
                    print('|   ', end = '|')
                else:
                    print('WWWW', end = '')
            print('WW', end = 'W')
            for x in range(0,width):
                if x == n:
                    print('|   ', end = '|')
                else:
                    print('WWWW', end = '')#this last section puts the passage between the grids
        print()
def lists():
    global room1
    global room2
    global room3
    global room4
    global room5
    global room6
    global room7
    global room8
    global room9
    global user
    global userPosition
    n = 5#edit this number too
    room1 = []
    for i in range(0,n):
        room1.append(['   '] * n)
    room2 = []
    for i in range(0,n):
        room2.append(['   '] * n)
    room3 = []
    for i in range(0,n):
        room3.append(['   '] * n)
    room4 = []
    for i in range(0,n):
        room4.append(['   '] * n)
    room5 = []
    for i in range(0,n):
        room5.append(['   '] * n)
    room6 = []
    for i in range(0,n):
        room6.append(['   '] * n)
    room7 = []
    for i in range(0,n):
        room7.append(['   '] * n)
    room8 = []
    for i in range(0,n):
        room8.append(['   '] * n)
    room9 = []
    for i in range(0,n):
        room9.append(['   '] * n)
    room5[2][2] = user
    userPosition = 'room522'#this is the players current coodinate
def doorCheck(x,userMove):
    global userPosition
    door1 = '02'#clockwise starting at 12 O'clock, then 3 O'clock,
    door2 = '24'#                      then 6 O'clock, then 9 O'clock
    door3 = '42'
    door4 = '20'
    if ('room' + str(x)) == 'room1':#<-----------ROOM 1
        if userPosition == ('room1' + door2) or userPosition == ('room1' + door3):  
            if userMove == 'S' and userPosition == ('room1' + door3):#moving down through door 3 '42'
                doorMove = doorMover()
                if doorMove == 'y':
                    room4[0][2] = user#changes the next square to the 'P'
                    room1[4][2] = '   '
                    userPosition = 'room4' + door1
                    return True
                else:
                    return 'NoDoor'
            elif userMove == 'D' and userPosition == ('room1' + door2):#moving right through door 2 '24'
                doorMove = doorMover()
                if doorMove == 'y':
                    room2[2][0] = user#changes the next square to the 'P'
                    room1[2][4] = '   '
                    userPosition = 'room2' + door4
                    return True
                else:
                    return 'NoDoor'
            else:
                return False
        else:
            return False
    elif ('room' + str(x)) == 'room2':#<-----------ROOM 2
        if userPosition == ('room2' + door2) or userPosition == ('room2' + door3) or userPosition == ('room2' + door4):
            if userMove == 'A' and userPosition == ('room2' + door4):#moving left through door 4 '20'
                doorMove = doorMover()
                if doorMove == 'y':
                    room1[2][4] = user#changes the next square to the 'P'
                    room2[2][0] = '   '
                    userPosition = 'room1' + door2
                    return True
                else:
                    return 'NoDoor'   
            elif userMove == 'S' and userPosition == ('room2' + door3):#moving down through door 3 '42'
                doorMove = doorMover()
                if doorMove == 'y':
                    room5[0][2] = user#changes the next square to the 'P'
                    room2[4][2] = '   '
                    userPosition = 'room5' + door1
                    return True
                else:
                    return 'NoDoor'
            elif userMove == 'D' and userPosition == ('room2' + door2):#moving right through door 2 '24'
                doorMove = doorMover()
                if doorMove == 'y':
                    room3[2][0] = user#changes the next square to the 'P'
                    room2[2][4] = '   '
                    userPosition = 'room3' + door4
                    return True
                else:
                    return 'NoDoor'
            else:
                return False
        else:
            return False
    elif ('room' + str(x)) == 'room3':#<-----------ROOM 3
        if userPosition == ('room3' + door3) or userPosition == ('room3' + door4):
            if userMove == 'A' and userPosition == ('room3' + door4):#moving left through door 4 '20'
                doorMove = doorMover()
                if doorMove == 'y':
                    room2[2][4] = user#changes the next square to the 'P'
                    room3[2][0] = '   '
                    userPosition = 'room4' + door2
                    return True
                else:
                    return 'NoDoor'   
            elif userMove == 'S' and userPosition == ('room3' + door3):#moving down through door 3 '42'
                doorMove = doorMover()
                if doorMove == 'y':
                    room6[0][2] = user#changes the next square to the 'P'
                    room3[4][2] = '   '
                    userPosition = 'room6' + door1
                    return True
                else:
                    return 'NoDoor'
            else:
                return False
        else:
            return False
    elif ('room' + str(x)) == 'room4':#<-----------ROOM 4
        if userPosition == ('room4' + door1) or userPosition == ('room4' + door2)or\
           userPosition == ('room4' + door3) or userPosition == ('room4' + door4):
            if userMove == 'W' and userPosition == ('room4' + str(door1)):#moving up through door 1 '02'
                doorMove = doorMover()
                if doorMove == 'y':
                    room1[4][2] = user#changes the next square to the 'P'
                    room4[0][2] = '   '
                    userPosition = 'room1' + door3
                    return True
                else:
                    return 'NoDoor'     
            elif userMove == 'S' and userPosition == ('room4' + door3):#moving down through door 3 '42'
                doorMove = doorMover()
                if doorMove == 'y':
                    room7[0][2] = user#changes the next square to the 'P'
                    room4[4][2] = '   '
                    userPosition = 'room7' + door1
                    return True
                else:
                    return 'NoDoor'
            elif userMove == 'D' and userPosition == ('room4' + door2):#moving right through door 2 '24'
                doorMove = doorMover()
                if doorMove == 'y':
                    room5[2][0] = user#changes the next square to the 'P'
                    room4[2][4] = '   '
                    userPosition = 'room5' + door4
                    return True
                else:
                    return 'NoDoor'
            else:
                return False
        else:
            return False
    elif ('room' + str(x)) == 'room5':#<-----------ROOM 5
        if userPosition == ('room5' + door1) or userPosition == ('room5' + door2)or\
           userPosition == ('room5' + door3) or userPosition == ('room5' + door4):
            if userMove == 'W' and userPosition == ('room5' + str(door1)):#moving up through door 1 '02'
                doorMove = doorMover()
                if doorMove == 'y':
                    room2[4][2] = user#changes the next square to the 'P'
                    room5[0][2] = '   '
                    userPosition = 'room2' + door3
                    return True
                else:
                    return 'NoDoor'   
            elif userMove == 'A' and userPosition == ('room5' + door4):#moving left through door 4 '20'
                doorMove = doorMover()
                if doorMove == 'y':
                    room4[2][4] = user#changes the next square to the 'P'
                    room5[2][0] = '   '
                    userPosition = 'room4' + door2
                    return True
                else:
                    return 'NoDoor'   
            elif userMove == 'S' and userPosition == ('room5' + door3):#moving down through door 3 '42'
                doorMove = doorMover()
                if doorMove == 'y':
                    room8[0][2] = user#changes the next square to the 'P'
                    room5[4][2] = '   '
                    userPosition = 'room8' + door1
                    return True
                else:
                    return 'NoDoor'
            elif userMove == 'D' and userPosition == ('room5' + door2):#moving right through door 2 '24'
                doorMove = doorMover()
                if doorMove == 'y':
                    room6[2][0] = user#changes the next square to the 'P'
                    room5[2][4] = '   '
                    userPosition = 'room6' + door4
                    return True
                else:
                    return 'NoDoor'
            else:
                return False
        else:
            return False
    elif ('room' + str(x)) == 'room6':#<-----------ROOM 6
        if userPosition == ('room6' + door1) or userPosition == ('room6' + door3) or userPosition == ('room6' + door4):
            if userMove == 'W' and userPosition == ('room6' + str(door1)):#moving up through door 1 '02'
                doorMove = doorMover()
                if doorMove == 'y':
                    room3[4][2] = user#changes the next square to the 'P'
                    room6[0][2] = '   '
                    userPosition = 'room3' + door3
                    return True
                else:
                    return 'NoDoor'   
            elif userMove == 'A' and userPosition == ('room6' + door4):#moving left through door 4 '20'
                doorMove = doorMover()
                if doorMove == 'y':
                    room5[2][4] = user#changes the next square to the 'P'
                    room6[2][0] = '   '
                    userPosition = 'room5' + door2
                    return True
                else:
                    return 'NoDoor'   
            elif userMove == 'S' and userPosition == ('room6' + door3):#moving down through door 3 '42'
                doorMove = doorMover()
                if doorMove == 'y':
                    room9[0][2] = user#changes the next square to the 'P'
                    room6[4][2] = '   '
                    userPosition = 'room9' + door1
                    return True
                else:
                    return 'NoDoor'
            else:
                return False
        else:
            return False
    elif ('room' + str(x)) == 'room7':#<-----------ROOM 7
        if userPosition == ('room7' + door1) or userPosition == ('room7' + door2)or\
           userPosition == ('room7' + door3) or userPosition == ('room7' + door4):
            if userMove == 'W' and userPosition == ('room7' + str(door1)):#moving up through door 1 '02'
                doorMove = doorMover()
                if doorMove == 'y':
                    room4[4][2] = user#changes the next square to the 'P'
                    room7[0][2] = '   '
                    userPosition = 'room4' + door3
                    return True
                else:
                    return 'NoDoor'   
            elif userMove == 'D' and userPosition == ('room7' + door2):#moving right through door 2 '24'
                doorMove = doorMover()
                if doorMove == 'y':
                    room8[2][0] = user#changes the next square to the 'P'
                    room7[2][4] = '   '
                    userPosition = 'room8' + door4
                    return True
                else:
                    return 'NoDoor'
            else:
                return False
        else:
            return False
    elif ('room' + str(x)) == 'room8':#<-----------ROOM 8
        if userPosition == ('room8' + door1) or userPosition == ('room8' + door2)or\
           userPosition == ('room8' + door3) or userPosition == ('room8' + door4):
            if userMove == 'W' and userPosition == ('room8' + str(door1)):#moving up through door 1 '02'
                doorMove = doorMover()
                if doorMove == 'y':
                    room5[4][2] = user#changes the next square to the 'P'
                    room8[0][2] = '   '
                    userPosition = 'room2' + door3
                    return True
                else:
                    return 'NoDoor'   
            elif userMove == 'A' and userPosition == ('room8' + door4):#moving left through door 4 '20'
                doorMove = doorMover()
                if doorMove == 'y':
                    room7[2][4] = user#changes the next square to the 'P'
                    room8[2][0] = '   '
                    userPosition = 'room4' + door2
                    return True
                else:
                    return 'NoDoor' 
            elif userMove == 'D' and userPosition == ('room8' + door2):#moving right through door 2 '24'
                doorMove = doorMover()
                if doorMove == 'y':
                    room9[2][0] = user#changes the next square to the 'P'
                    room8[2][4] = '   '
                    userPosition = 'room6' + door4
                    return True
                else:
                    return 'NoDoor'
            else:
                return False
        else:
            return False
    elif ('room' + str(x)) == 'room9':#<-----------ROOM 9
        if userPosition == ('room9' + door1) or userPosition == ('room9' + door2)or\
           userPosition == ('room9' + door3) or userPosition == ('room9' + door4):
            if userMove == 'W' and userPosition == ('room9' + str(door1)):#moving up through door 1 '02'
                doorMove = doorMover()
                if doorMove == 'y':
                    room6[4][2] = user#changes the next square to the 'P'
                    room9[0][2] = '   '
                    userPosition = 'room6' + door3
                    return True
                else:
                    return 'NoDoor'   
            elif userMove == 'A' and userPosition == ('room9' + door4):#moving left through door 4 '20'
                doorMove = doorMover()
                if doorMove == 'y':
                    room8[2][4] = user#changes the next square to the 'P'
                    room9[2][0] = '   '
                    userPosition = 'room8' + door2
                    return True
                else:
                    return 'NoDoor'
            else:
                return False
        else:
            return False
    else:
        print('User Position FAIL')
def doorMover():
        return 'y'
def newPosition(y, x, userMove,roomNum,roomNum1):
    global user
    global userPosition
    if userMove == 'W':
        if y != 0:
            yOld = y
            y -= 1
            roomNum[yOld][x] = '   '
        else:
            print('No matter how hard you try you CANNOT walk through the wall!')
    elif userMove == 'A':
        if x != 0:
            xOld = x
            x -= 1
            roomNum[y][xOld] = '   '
        else:
            print('No matter how hard you try you CANNOT walk through the wall!')
    elif userMove == 'S':
        if y != 4:
            yOld = y
            y += 1
            roomNum[yOld][x] = '   '
        else:
            print('No matter how hard you try you CANNOT walk through the wall!')
    elif userMove == 'D':
        if x != 4:
            xOld = x
            x += 1
            roomNum[y][xOld] = '   '
        else:
            print('No matter how hard you try you CANNOT walk through the wall!')
    roomNum[y][x] = user#changes the next square to the 'P'
    return 'room' + roomNum1 + str(y) + str(x)
def gamePlay():#y,x
    global room1
    global room2
    global room3
    global room4
    global room5
    global room6
    global room7
    global room8
    global room9
    global userPosition
    global user
    n = 5
    userIN = False
    newCoord = False
    loop = 0
    y = 0
    x = 0
    while userIN == False:
        userInput = input('Where do you want to move?(w,a,s,d)\n   or "quit" to end the game: ').lower()
        if userInput in ['w', 'a', 's', 'd']:
            userMove = userInput.upper()
            userIN = True
        elif userInput == 'quit':
            print('Ok Goodbye...')
            time.sleep(1)
            sys.exit()
        else:
            print('Try Again')
    if user in room1[0] or user in room1[1] or user in room1[2] or user in room1[3] or user in room1[4]:
        roomNum = room1
        a = 1
    elif user in room2[0] or user in room2[1] or user in room2[2] or user in room2[3] or user in room2[4]:
        roomNum = room2
        a = 2
    elif user in room3[0] or user in room3[1] or user in room3[2] or user in room3[3] or user in room3[4]:
        roomNum = room3
        a = 3
    elif user in room4[0] or user in room4[1] or user in room4[2] or user in room4[3] or user in room4[4]:
        roomNum = room4
        a = 4
    elif user in room5[0] or user in room5[1] or user in room5[2] or user in room5[3] or user in room5[4]:
        roomNum = room5
        a = 5
    elif user in room6[0] or user in room6[1] or user in room6[2] or user in room6[3] or user in room6[4]:
        roomNum = room6
        a = 6
    elif user in room7[0] or user in room7[1] or user in room7[2] or user in room7[3] or user in room7[4]:
        roomNum = room7
        a = 7
    elif user in room8[0] or user in room8[1] or user in room8[2] or user in room8[3] or user in room8[4]:
        roomNum = room8
        a = 8
    elif user in room9[0] or user in room9[1] or user in room9[2] or user in room9[3] or user in room9[4]:
        roomNum = room9
        a = 9
    while newCoord == False:
        while loop < n and newCoord == False:
            if user == roomNum[y][x]:
                door = doorCheck(a, userMove)
                if door == True:
                    print('You enter through the door...')
                    newCoord = True
                    loop = 0
                    y = 0
                    x = 0
                elif door == False:
                    userPosition = newPosition(y, x, userMove, roomNum, str(a))
                    newCoord = True
                    loop = 0
                    y = 0
                    x = 0
                elif door == 'NoDoor':
                    print('You decide to stay put for now.')
                    newCoord = True
                    loop = 0
                    y = 0
                    x = 0
            x += 1
            loop += 1
        y += 1
        loop = 0
        x = 0
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    lists()
    gameOver = False
    while gameOver == False:
        grid()
        gamePlay()
