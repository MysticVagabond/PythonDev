import sys
while True:
    a = ['0','1']
    userIn = input('\nType e to Exit or a number\nN: ')
    if userIn in 'e E q Q'.split():
        sys.exit()
    if userIn.isdigit():
        for num in range(int(userIn) - 1):
            b = list(a)
            b.reverse()
            for x in range(len(a)):
                a[x] = '0' + a[x]
            for y in range(len(b)):
                b[y] = '1' + b[y]
            temp = []
            for z in range(len(a)):
                temp.append(a[z])
            if userIn != '1':
                for q in range(len(b)):
                    temp.append(b[q])
            a = list(temp)
        if userIn == '1':
            temp = a
        print('\n' + str(userIn) + ' bit Gray Code:')
        for i in range(len(temp)):
            if int(userIn) >= 6:
                print(str(temp[i]), end = ' ')
            else:
                print(str(i + 1) + ' ' + str(temp[i]))
        print()
