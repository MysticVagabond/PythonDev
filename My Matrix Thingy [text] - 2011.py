#Authors: Stephen Fisher and Roberto Dyke:D
#converts into Denary using the ASCII code then to binary
import random
import time
#the output from the Denary converter
outputDen0 = ''
outputDen1 = ''
outputDen2 = ''
outputDen3 = ''
outputDen4 = ''
outputDen5 = ''
outputDen6 = ''
outputDen7 = ''
outputDen8 = ''
outputDen9 = ''
outputDen10 = ''
outputDen11 = ''
denOut = ''
#the output from the binary converter
outputBin1 = ''
outputBin2 = ''
outputBin3 = ''
outputBin4 = ''
outputBin5 = ''
outputBin6 = ''
outputBin7 = ''
outputBin8 = ''
outputBin9 = ''
outputBin10 = ''
outputBin11 = ''
binOut = ''
#the output from the crazynumber random generator
crazy1 = ''
crazy2 = ''
crazy3 = ''
crazy4 = ''
crazy5 = ''
crazy6 = ''
crazy7 = ''
crazy8 = ''
crazyNumber = '0'
#the output from the find number generator
find1 = ''
find2 = ''
find3 = ''
find4 = ''
find5 = ''
find6 = ''
find7 = ''
find8 = ''
findNum = ''
#final random generators bit: while statement start positions
found1 = False
found2 = False
found3 = False
found4 = False
found5 = False
found6 = False
found7 = False
found8 = False
found9 = False
found10 = False
found11 = False
foundAll = False
def convertDenary():#this is the library for the list of letters
    global denOut
    if (letter == "a"):
        denOut = 97
    elif (letter == "b"):
        denOut = 98
    elif (letter == "c"):
        denOut = 99
    elif (letter == "d"):
        denOut = 100
    elif (letter == "e"):
        denOut = 101
    elif (letter == "f"):
        denOut = 102
    elif (letter == "g"):
        denOut = 103
    elif (letter == "h"):
        denOut = 104
    elif (letter == "i"):
        denOut = 105
    elif (letter == "j"):
        denOut = 106
    elif (letter == "k"):
        denOut = 107
    elif (letter == "l"):
        denOut = 108
    elif (letter == "m"):
        denOut = 109
    elif (letter == "n"):
        denOut = 110
    elif (letter == "o"):
        denOut = 111
    elif (letter == "p"):
        denOut = 112
    elif (letter == "q"):
        denOut = 113
    elif (letter == "r"):
        denOut = 114
    elif (letter == "s"):
        denOut = 115
    elif (letter == "t"):
        denOut = 116
    elif (letter == "u"):
        denOut = 117
    elif (letter == "v"):
        denOut = 118
    elif (letter == "w"):
        denOut = 119
    elif (letter == "x"):
        denOut = 120
    elif (letter == "y"):
        denOut = 121
    elif (letter == "z"):
        denOut = 122
    else:
        print("Roberto's so cool that this don't even work...\n    Error 1           :)")
def denOut1():#this assigns a variable name to each letter
    global outputDen1
    global outputDen2
    global outputDen3
    global outputDen4
    global outputDen5
    global outputDen6
    global outputDen7
    global outputDen8
    global outputDen9
    global outputDen10
    global outputDen11
    if (denCycle == 0):
        outputDen1 = denOut
    elif (denCycle == 1):
        outputDen2 = denOut
    elif (denCycle == 2):
        outputDen3 = denOut
    elif (denCycle == 3):
        outputDen4 = denOut
    elif (denCycle == 4):
        outputDen5 = denOut
    elif (denCycle == 5):
        outputDen6 = denOut
    elif (denCycle == 6):
        outputDen7 = denOut
    elif (denCycle == 7):
        outputDen8 = denOut
    elif (denCycle == 8):
        outputDen9 = denOut
    elif (denCycle == 9):
        outputDen10 = denOut
    elif (denCycle == 10):
        outputDen11 = denOut
    else:
        print("Error 2 denOut")  
    outputDen1 = str(outputDen1)
    outputDen2 = str(outputDen2)
    outputDen3 = str(outputDen3)
    outputDen4 = str(outputDen4)
    outputDen5 = str(outputDen5)
    outputDen6 = str(outputDen6)
    outputDen7 = str(outputDen7)
    outputDen8 = str(outputDen8)
    outputDen9 = str(outputDen9)
    outputDen10 = str(outputDen10)
    outputDen11 = str(outputDen11)
def convertBinary():#this is the library for the list of binary numbers
    global binOut
    if (binary == "97"):
        binOut = "01100001"
    elif (binary == "98"):
        binOut = "01100010"
    elif (binary == "99"):
        binOut = "01100011"
    elif (binary == "100"):
        binOut = "01100100"
    elif (binary == "101"):
        binOut = "01100101"
    elif (binary == "102"):
        binOut = "01100110"
    elif (binary == "103"):
        binOut = "01100111"
    elif (binary == "104"):
        binOut = "01101000"
    elif (binary == "105"):
        binOut = "01101001"
    elif (binary == "106"):
        binOut = "01101010"
    elif (binary == "107"):
        binOut = "01101011"
    elif (binary == "108"):
        binOut = "01101100"
    elif (binary == "109"):
        binOut = "01101101"
    elif (binary == "110"):
        binOut = "01101110"
    elif (binary == "111"):
        binOut = "01101111"
    elif (binary == "112"):
        binOut = "01110000"
    elif (binary == "113"):
        binOut = "01110001"
    elif (binary == "114"):
        binOut = "01110010"
    elif (binary == "115"):
        binOut = "01110011"
    elif (binary == "116"):
        binOut = "01110100"
    elif (binary == "117"):
        binOut = "01110101"
    elif (binary == "118"):
        binOut = "01110110"
    elif (binary == "119"):
        binOut = "01110111"
    elif (binary == "120"):
        binOut = "01111000"
    elif (binary == "121"):
        binOut = "01110001"
    elif (binary == "122"):
        binOut = "01111010"
    elif (binary == ''):
        binOut = ''
    else:
        print("Roberto's so cool that this don't even work...\n    Error 3           :)")
def binOut1():#this assigns a variable name to each binary number
    global outputBin1
    global outputBin2
    global outputBin3
    global outputBin4
    global outputBin5
    global outputBin6
    global outputBin7
    global outputBin8
    global outputBin9
    global outputBin10
    global outputBin11
    if (binCycle == 0):
        outputBin0 = ''
    elif (binCycle == 1):
        outputBin1 = binOut
    elif (binCycle == 2):
        outputBin2 = binOut
    elif (binCycle == 3):
        outputBin3 = binOut
    elif (binCycle == 4):
        outputBin4 = binOut
    elif (binCycle == 5):
        outputBin5 = binOut
    elif (binCycle == 6):
        outputBin6 = binOut
    elif (binCycle == 7):
        outputBin7 = binOut
    elif (binCycle == 8):
        outputBin8 = binOut
    elif (binCycle == 9):
        outputBin9 = binOut
    elif (binCycle == 10):
        outputBin10 = binOut
    elif (binCycle == 11):
        outputBin11 = binOut
    else:
        print("Error 4 binOut")
    outputBin1 = str(outputBin1)
    outputBin2 = str(outputBin2)
    outputBin3 = str(outputBin3)
    outputBin4 = str(outputBin4)
    outputBin5 = str(outputBin5)
    outputBin6 = str(outputBin6)
    outputBin7 = str(outputBin7)
    outputBin8 = str(outputBin8)
    outputBin9 = str(outputBin9)
    outputBin10 = str(outputBin10)
    outputBin11 = str(outputBin11)
def crazyNums():
    global crazy1
    global crazy2
    global crazy3
    global crazy4
    global crazy5
    global crazy6
    global crazy7
    global crazy8
    global crazyNumber
    crazy1 = random.randint(0,1)
    crazy2 = random.randint(0,1)
    crazy3 = random.randint(0,1)
    crazy4 = random.randint(0,1)
    crazy5 = random.randint(0,1)
    crazy6 = random.randint(0,1)
    crazy7 = random.randint(0,1)
    crazy8 = random.randint(0,1)
    crazy1 = str(crazy1)
    crazy1 = str(crazy2)
    crazy1 = str(crazy3)
    crazy1 = str(crazy4)
    crazy1 = str(crazy5)
    crazy1 = str(crazy6)
    crazy1 = str(crazy7)
    crazy1 = str(crazy8)
def findNumber():
    global find1
    global find2
    global find3
    global find4
    global find5
    global find6
    global find7
    global find8
    global findNum
    find1 = random.randint(0,1)
    find2 = random.randint(0,1)
    find3 = random.randint(0,1)
    find4 = random.randint(0,1)
    find5 = random.randint(0,1)
    find6 = random.randint(0,1)
    find7 = random.randint(0,1)
    find8 = random.randint(0,1)
    find1 = str(find1)
    find2 = str(find2)
    find3 = str(find3)
    find4 = str(find4)
    find5 = str(find5)
    find6 = str(find6)
    find7 = str(find7)
    find8 = str(find8)
    findNum = (find1 + find2 + find3 + find4 + find5 + find6 + find7 + find8)
letDen = 0  #<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--this is where the program starts
denBin = 0
denCycle = 0
binCycle = 0
loop = 0
print('Hello User\n What is your name?\n(9 characters max)')
fullName = input()
fullName = fullName.lower()#this next bit converts the name into lowercase letters and then a list
letterList = list(fullName)
length = len(fullName)
length1 = length + 1
while letDen < length:      #this uses the Denary converter
    letter = letterList[denCycle]
    convertDenary()
    denOut1()
    denCycle += 1
    letDen += 1
denaryList = (outputDen0),(outputDen1),(outputDen2),(outputDen3),(outputDen4),(outputDen5),(outputDen6),(outputDen7),(outputDen8),(outputDen9),(outputDen10)
while denBin < length1:     #this uses the Binary converter
    binary = denaryList[binCycle]
    convertBinary()
    binOut1()
    binCycle += 1
    denBin += 1
while loop < 10:#<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--    this is where the number finding starts
    crazyNums()
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#1
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#2
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#3
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#4
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#5
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#6
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#7
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#8
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8)#9
    loop += 1
while found1 == False:          #<--<--<--<--find number 1
    findNumber()
    crazyNums()
    print(find1, find2, find3, find4, find5, find6, find7, find8, end = ' ')#1
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#2
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#3
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#4
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#5
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#6
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#7
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#8
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8)#9
    if findNum == outputBin1:
        letter11 = find1    #this is letter1.1
        letter12 = find2
        letter13 = find3
        letter14 = find4
        letter15 = find5
        letter16 = find6
        letter17 = find7
        letter18 = find8    #this is letter1.8
        found1 = True
    elif outputBin1 == '':
        found1 = True
        letter11 = crazy1    #this is letter1.1
        letter12 = crazy2
        letter13 = crazy3
        letter14 = crazy4
        letter15 = crazy5
        letter16 = crazy6
        letter17 = crazy7
        letter18 = crazy8    #this is letter1.8
while found2 == False:          #<--<--<--<--find number 2
    findNumber()
    crazyNums()
    print(letter11, letter12, letter13, letter14, letter15, letter16, letter17, letter18, end = ' ')#1
    print(find1, find2, find3, find4, find5, find6, find7, find8, end = ' ')#2
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#3
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#4
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#5
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#6
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#7
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#8
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8)#9
    if findNum == outputBin2:
        letter21 = find1    #this is letter2.1
        letter22 = find2
        letter23 = find3
        letter24 = find4
        letter25 = find5
        letter26 = find6
        letter27 = find7
        letter28 = find8    #this is letter2.8
        found2 = True
    elif outputBin2 == '':
        found2 = True
        letter21 = crazy1    #this is letter2.1
        letter22 = crazy2
        letter23 = crazy3
        letter24 = crazy4
        letter25 = crazy5
        letter26 = crazy6
        letter27 = crazy7
        letter28 = crazy8    #this is letter2.8
while found3 == False:          #<--<--<--<--find number 3
    findNumber()
    crazyNums()
    print(letter11, letter12, letter13, letter14, letter15, letter16, letter17, letter18, end = ' ')#1
    print(letter21, letter22, letter23, letter24, letter25, letter26, letter27, letter28, end = ' ')#2
    print(find1, find2, find3, find4, find5, find6, find7, find8, end = ' ')#3
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#4
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#5
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#6
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#7
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#8
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8)#9
    if findNum == outputBin3:
        letter31 = find1    #this is letter3.1
        letter32 = find2
        letter33 = find3
        letter34 = find4
        letter35 = find5
        letter36 = find6
        letter37 = find7
        letter38 = find8    #this is letter3.8
        found3 = True
    elif outputBin3 == '':
        found3 = True
        letter31 = crazy1    #this is letter3.1
        letter32 = crazy2
        letter33 = crazy3
        letter34 = crazy4
        letter35 = crazy5
        letter36 = crazy6
        letter37 = crazy7
        letter38 = crazy8    #this is letter3.8
while found4 == False:          #<--<--<--<--find number 4
    findNumber()
    crazyNums()
    print(letter11, letter12, letter13, letter14, letter15, letter16, letter17, letter18, end = ' ')#1
    print(letter21, letter22, letter23, letter24, letter25, letter26, letter27, letter28, end = ' ')#2
    print(letter31, letter32, letter33, letter34, letter35, letter36, letter37, letter38, end = ' ')#3
    print(find1, find2, find3, find4, find5, find6, find7, find8, end = ' ')#4
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#5
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#6
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#7
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#8
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8)#9
    if findNum == outputBin4:
        letter41 = find1    #this is letter5.1
        letter42 = find2
        letter43 = find3
        letter44 = find4
        letter45 = find5
        letter46 = find6
        letter47 = find7
        letter48 = find8    #this is letter5.8
        found4 = True
    elif outputBin4 == '':
        found4 = True
        letter41 = crazy1    #this is letter4.1
        letter42 = crazy2
        letter43 = crazy3
        letter44 = crazy4
        letter45 = crazy5
        letter46 = crazy6
        letter47 = crazy7
        letter48 = crazy8    #this is letter4.8
while found5 == False:          #<--<--<--<--find number 5
    findNumber()
    crazyNums()
    print(letter11, letter12, letter13, letter14, letter15, letter16, letter17, letter18, end = ' ')#1
    print(letter21, letter22, letter23, letter24, letter25, letter26, letter27, letter28, end = ' ')#2
    print(letter31, letter32, letter33, letter34, letter35, letter36, letter37, letter38, end = ' ')#3
    print(letter41, letter42, letter43, letter44, letter45, letter46, letter47, letter48, end = ' ')#4
    print(find1, find2, find3, find4, find5, find6, find7, find8, end = ' ')#5
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#6
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#7
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#8
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8)#9
    if findNum == outputBin5:
        letter51 = find1    #this is letter5.1
        letter52 = find2
        letter53 = find3
        letter54 = find4
        letter55 = find5
        letter56 = find6
        letter57 = find7
        letter58 = find8    #this is letter5.8
        found5 = True
    elif outputBin5 == '':
        found5 = True
        letter51 = crazy1    #this is letter5.1
        letter52 = crazy2
        letter53 = crazy3
        letter54 = crazy4
        letter55 = crazy5
        letter56 = crazy6
        letter57 = crazy7
        letter58 = crazy8    #this is letter5.8
while found6 == False:          #<--<--<--<--find number 6
    findNumber()
    crazyNums()
    print(letter11, letter12, letter13, letter14, letter15, letter16, letter17, letter18, end = ' ')#1
    print(letter21, letter22, letter23, letter24, letter25, letter26, letter27, letter28, end = ' ')#2
    print(letter31, letter32, letter33, letter34, letter35, letter36, letter37, letter38, end = ' ')#3
    print(letter41, letter42, letter43, letter44, letter45, letter46, letter47, letter48, end = ' ')#4
    print(letter51, letter52, letter53, letter54, letter55, letter56, letter57, letter58, end = ' ')#5
    print(find1, find2, find3, find4, find5, find6, find7, find8, end = ' ')#6
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#7
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#8
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8)#9
    if findNum == outputBin6:
        letter61 = find1    #this is letter6.1
        letter62 = find2
        letter63 = find3
        letter64 = find4
        letter65 = find5
        letter66 = find6
        letter67 = find7
        letter68 = find8    #this is letter6.8
        found6 = True
    elif outputBin6 == '':
        found6 = True
        letter61 = crazy1    #this is letter6.1
        letter62 = crazy2
        letter63 = crazy3
        letter64 = crazy4
        letter65 = crazy5
        letter66 = crazy6
        letter67 = crazy7
        letter68 = crazy8    #this is letter6.8
while found7 == False:          #<--<--<--<--find number 7
    findNumber()
    crazyNums()
    print(letter11, letter12, letter13, letter14, letter15, letter16, letter17, letter18, end = ' ')#1
    print(letter21, letter22, letter23, letter24, letter25, letter26, letter27, letter28, end = ' ')#2
    print(letter31, letter32, letter33, letter34, letter35, letter36, letter37, letter38, end = ' ')#3
    print(letter41, letter42, letter43, letter44, letter45, letter46, letter47, letter48, end = ' ')#4
    print(letter51, letter52, letter53, letter54, letter55, letter56, letter57, letter58, end = ' ')#5
    print(letter61, letter62, letter63, letter64, letter65, letter66, letter67, letter68, end = ' ')#6
    print(find1, find2, find3, find4, find5, find6, find7, find8, end = ' ')#7
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8, end = ' ')#8
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8)#9
    if findNum == outputBin7:
        letter71 = find1    #this is letter7.1
        letter72 = find2
        letter73 = find3
        letter74 = find4
        letter75 = find5
        letter76 = find6
        letter77 = find7
        letter78 = find8    #this is letter7.8
        found7 = True
    elif outputBin7 == '':
        found7 = True
        letter71 = crazy1    #this is letter7.1
        letter72 = crazy2
        letter73 = crazy3
        letter74 = crazy4
        letter75 = crazy5
        letter76 = crazy6
        letter77 = crazy7
        letter78 = crazy8    #this is letter7.8
while found8 == False:          #<--<--<--<--find number 8
    findNumber()
    crazyNums()
    print(letter11, letter12, letter13, letter14, letter15, letter16, letter17, letter18, end = ' ')#1
    print(letter21, letter22, letter23, letter24, letter25, letter26, letter27, letter28, end = ' ')#2
    print(letter31, letter32, letter33, letter34, letter35, letter36, letter37, letter38, end = ' ')#3
    print(letter41, letter42, letter43, letter44, letter45, letter46, letter47, letter48, end = ' ')#4
    print(letter51, letter52, letter53, letter54, letter55, letter56, letter57, letter58, end = ' ')#5
    print(letter61, letter62, letter63, letter64, letter65, letter66, letter67, letter68, end = ' ')#6
    print(letter71, letter72, letter73, letter74, letter75, letter76, letter77, letter78, end = ' ')#7
    print(find1, find2, find3, find4, find5, find6, find7, find8, end = ' ')#8
    print(crazy1, crazy2, crazy3, crazy4, crazy5, crazy6, crazy7, crazy8)#9
    if findNum == outputBin8:
        letter81 = find1    #this is letter8.1
        letter82 = find2
        letter83 = find3
        letter84 = find4
        letter85 = find5
        letter86 = find6
        letter87 = find7
        letter88 = find8    #this is letter8.8
        found8 = True
    elif outputBin8 == '':
        found8 = True
        letter81 = crazy1    #this is letter8.1
        letter82 = crazy2
        letter83 = crazy3
        letter84 = crazy4
        letter85 = crazy5
        letter86 = crazy6
        letter87 = crazy7
        letter88 = crazy8    #this is letter8.8
while found9 == False:          #<--<--<--<--find number 9
    findNumber()
    crazyNums()
    print(letter11, letter12, letter13, letter14, letter15, letter16, letter17, letter18, end = ' ')#1
    print(letter21, letter22, letter23, letter24, letter25, letter26, letter27, letter28, end = ' ')#2
    print(letter31, letter32, letter33, letter34, letter35, letter36, letter37, letter38, end = ' ')#3
    print(letter41, letter42, letter43, letter44, letter45, letter46, letter47, letter48, end = ' ')#4
    print(letter51, letter52, letter53, letter54, letter55, letter56, letter57, letter58, end = ' ')#5
    print(letter61, letter62, letter63, letter64, letter65, letter66, letter67, letter68, end = ' ')#6
    print(letter71, letter72, letter73, letter74, letter75, letter76, letter77, letter78, end = ' ')#7
    print(letter81, letter82, letter83, letter84, letter85, letter86, letter87, letter88, end = ' ')#8
    print(find1, find2, find3, find4, find5, find6, find7, find8)#9
    if findNum == outputBin9:
        letter91 = find1    #this is letter9.1
        letter92 = find2
        letter93 = find3
        letter94 = find4
        letter95 = find5
        letter96 = find6
        letter97 = find7
        letter98 = find8    #this is letter9.8
        found9 = True
    elif outputBin9 == '':
        found9 = True
        letter91 = crazy1    #this is letter9.1
        letter92 = crazy2
        letter93 = crazy3
        letter94 = crazy4
        letter95 = crazy5
        letter96 = crazy6
        letter97 = crazy7
        letter98 = crazy8    #this is letter9.8
print()
print()
print(letter11, letter12, letter13, letter14, letter15, letter16, letter17, letter18, end = ',')#1
print(letter21, letter22, letter23, letter24, letter25, letter26, letter27, letter28, end = ',')#2
print(letter31, letter32, letter33, letter34, letter35, letter36, letter37, letter38, end = ',')#3
print(letter41, letter42, letter43, letter44, letter45, letter46, letter47, letter48, end = ',')#4
print(letter51, letter52, letter53, letter54, letter55, letter56, letter57, letter58, end = ',')#5
print(letter61, letter62, letter63, letter64, letter65, letter66, letter67, letter68, end = ',')#6
print(letter71, letter72, letter73, letter74, letter75, letter76, letter77, letter78, end = ',')#7
print(letter81, letter82, letter83, letter84, letter85, letter86, letter87, letter88, end = ',')#8
print(letter91, letter92, letter93, letter94, letter95, letter96, letter97, letter98)#9
print()
time.sleep(1)
print('Your input of: ' + fullName)
print()
print('Makes   ' + outputBin1 + '  ' + outputBin2 + '  ' + outputBin3 + '  ' + outputBin4 + '  ' + outputBin5 + '  ' + outputBin6 + '  ' + outputBin7 + '  ' + outputBin8 + '  ' + outputBin9 + '    in Binary!')
time.sleep(1)
print('This is ' + '  ' +outputDen1 + '   ' + '  ' + '  ' + outputDen2 + '   ' + '  ' + '  ' + outputDen3 + '   ' + '  ' + '  ' + outputDen4 + '   ' + '  ' + '  ' + outputDen5 + '   ' + '  ' + '  ' + outputDen6 + '   ' + '  ' + '  ' + outputDen7 + '   ' + '  ' + '  ' + outputDen8 + '   ' + '  ' + '  ' + outputDen9 + '       using the ASCII code')
time.sleep(5)
print()
print("Press Return to exit the program")
exit = input()
