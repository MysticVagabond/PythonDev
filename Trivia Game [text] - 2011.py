questions = ['What is the capital of Spain','What is Spanish for hello?',\
             'What is the binary for 7?', 'What county is Ascot in?',\
             'How many days in a year', 'What is the chemical symbol for Lead',\
             'What is the chemical name for salt', 'What is the fastest time for the 100M sprint?',\
             'What is Calcium Carbonate normally known as?', 'Which animal produces the largest live baby?']
ans1 = ['Madrid', 'London', 'Paris', 'Berlin']
ans2 = ['Konnichiwa', 'Bonjour', 'Hola', 'Au Revoir']
ans3 = ['1000', '110', '111', '101']
ans4 = ['BuckinghamShire', 'West Sussex', 'Surrey', 'Berkshire']
ans5 = ['360', '365', '370', '367']
ans6 = ['L', 'Sn', 'Ld', 'Pb']
ans7 = ['Sodium Chloride', 'Sodium Sulphate', 'Copper Chloride', 'Zinc Sulphate']
ans8 = ['10.29 seconds', ' 9.58 seconds', '9.35 seconds', '8.97 seconds']
ans9 = ['Salt', 'Chalk', 'Coal', 'Milk']
ans10 = ['Elephant', 'Great White Shark', 'Polar Bears', 'Blue Whale']
alphabet = ['A', 'B', 'C', 'D']
answerList = [ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10]
ansCheck = ''
P1correctAns = 0
P2correctAns = 0
P1total = 0
P2total = 0
P1Q = 0
P2Q = 0#num of total questions
turn = 1
num = input('How many questions do you want to have each? (2-5)')
if num.isdigit():
    if 2 <= int(num) <= 5:
        numOfQuestions = int(num) * 2
else:
    print('Wrong, The game will default to 3 Questions each')
    numOfQuestions = 3
for i in range(0,numOfQuestions):
    if turn == 1:
        print('Player 1:')
        turn += 1
        P1Q += 1
    elif turn == 2:
        print('Player 2:')
        turn -= 1
        P2Q += 1
    print(questions[i])
    for s in range(0,len(ans1)):
        print('Answer', str(alphabet[s]), answerList[i][s])
    InputFound = False
    while InputFound == False:
        user = input('What is the answer?(A,B,C,D)')
        u = user.upper()
        if u == 'A' or u == 'B' or u == 'C' or u == 'D':
            InputFound = True
            userAnswer = user.upper()
        else:
            print('Try Again!')
    if i == 0:
        ansCheck = 'A'
    elif i == 1:
        ansCheck = 'C'
    elif i == 2:
        ansCheck = 'C'
    elif i == 3:
        ansCheck = 'D'
    elif i == 4:
        ansCheck = 'B'
    elif i == 5:
        ansCheck = 'D'
    elif i == 6:
        ansCheck = 'A'
    elif i == 7:
        ansCheck = 'B'
    elif i == 8:
        ansCheck = 'B'
    elif i == 9:
        ansCheck = 'D'
    else:
        print('FAILS')
    if userAnswer == ansCheck:
        print('Correct!')
        if turn == 1:
            P1correctAns += 1
        elif turn == 2:
            P2correctAns += 1
    elif userAnswer != ansCheck:
        print('Incorrect!')
    print()
print('Player 1:')
print('You got', P1correctAns, 'out of', P1Q)
P1percent = (P1correctAns / P1Q) * 100
print('That is', P1percent, '%')
if P1percent < 20:
    print('Not Good!')
elif 20 < P1percent < 80:
    print('Good Enough')
elif 80 < P1percent < 100:
    print('Well Done!')
print()
print('Player 2:')
print('You got', P2correctAns, 'out of', P2Q)
P2percent = (P2correctAns / P1Q) * 100
print('That is', P2percent, '%')
if P2percent < 20:
    print('Not Good!')
elif 20 < P2percent < 80:
    print('Good Enough')
elif 80 < P2percent < 100:
    print('Well Done!')
print()
if P1percent > P2percent:
    print('Player 1 Wins, Well Done!')
elif P2percent > P1percent:
    print('Player 2 Wins, Well Done!')
elif P1percent == P2percent:
    print('The game was a draw!')
input()
