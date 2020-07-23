import sys, time
sys.path.append('Project Files/Encrypter_V2/')
from EncryptScoreAndName import *
from DecryptScoreAndName import *

userName = 'Stephen'
encryptKey = 12
userScore = 100

def getMode():
    while True:
        print('Do you wish to "encrypt" or "decrypt" the message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        elif mode in 'exit quit q'.split():
            sys.exit()
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def encrypt(userName, encryptKey, userScore):
    print('Encrypting...')
    time.sleep(0.1)
    encodedName = createName(userName, encryptKey)
    encodedNum = createNumber(userScore)
    wholeEncryptedString = mergeNumAndString(encodedName, encodedNum, encryptKey)
    print('Name: %s, Number: %s, Encryption: %s' % (encodedName, encodedNum, wholeEncryptedString))

def decrypt(userInput):
    print('\nDecrypting...')
    time.sleep(0.1)
    key = userInput[:2]
    origName = userInput[2:]
    print('Key: %s, Encryption: %s' % (key, origName))
    name, number = unmergeNumAndString(origName)
    print('Separated Name: %s, Separated Number: %s' % (name, number))
    correctName = getName(name, key)
    correctScore = getNumber(number)
    print('Decrypted Name: %s \nDecrypted Score: %s' % (correctName, correctScore))

again = 'yes'
while again in 'yes y encrypt e decrypt d'.split():
    if again in 'yes y'.split():
        mode = getMode()
    else: mode = again[0]
    if mode[0] == 'e':
        userName = input('Your name:\n')
        userScore = int(input('Your score:\n'))
        encryptKey = int(input('Key to be used (a number between 1-25):\n'))
        while (encryptKey > 25) or (encryptKey < 0):
            if encryptKey > 26:
                encryptKey -= 26
            elif encryptKey < 0:
                encryptKey += 26

        encrypt(userName, encryptKey, userScore)
    else:
        userInput = input('Decrypted string:\n')

        decrypt(userInput)
        
    print('\nDo you want to encrypt or decrypt another message?(y/n)')
    again = input().lower()
