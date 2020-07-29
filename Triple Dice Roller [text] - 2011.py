import random
foundSix = False
n = 0
while foundSix == False:
    n += 1
    diceNum1 = random.randint(1,6)
    diceNum2 = random.randint(1,6)
    diceNum3 = random.randint(1,6)
    print(int(diceNum1), int(diceNum2), int(diceNum3),':', n)
    if(diceNum1 == 6) and (diceNum2 == 6) and (diceNum3 == 6):
        foundSix = True
print('Finished,\nPress return to exit')
exit = input()

