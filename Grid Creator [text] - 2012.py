def grid(x,y):
    width = x  #only edit these two numbers to edit grid dimensions
    height = y  #min 1 and max as many as will fit on the screen
    for z in range(0,height):
        for x in range(0,width):
            print('+---', end = '')
        print('+')
        print('|',end = '')
        for i in range(0,width):
            print('   |', end = '')
        print()
    for x in range(0,width):
        print('+---', end = '')
    print('+')
x = int(input('Type the width of the grid: '))
y = int(input('Type the height of the grid: '))
grid(x,y)
input()
