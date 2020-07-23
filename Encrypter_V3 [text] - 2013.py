import sys, time
sys.path.append('Project Files/Encrypter_V3/')
from Encrypter_3_1 import encryptSentenceClass
from Decrypter_3_1 import decryptSentenceClass

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

def encrypt():    
    Encrypter = encryptSentenceClass()#initialise the class to be able to access its functions
    sentence = input('Type sentence/word to encrypt: ')
    print('\nEncrypting...')
    sentence = Encrypter.encrypt(sentence)
    time.sleep(0.1)
    print(sentence,'\nDone')

def decrypt():
    Decrypter = decryptSentenceClass()#initialise the class to be able to access its functions  wordStr, numStr = Decrypter.separateWordsAndNumbers('05j0q5m0t0q0')
    sentence = input('Type sentence/word to decrypt: ')
    print('\nDecrypting...')
    sentence = Decrypter.decrypt(sentence)
    time.sleep(0.1)
    print(sentence,'\nDone')

again = 'yes'
while again in 'yes y encrypt e decrypt d'.split():
    if again in 'yes y'.split():
        mode = getMode()
    else: mode = again[0]
    if mode[0] == 'e':
        encrypt()
    else:
        decrypt()
        
    print('\nDo you want to encrypt or decrypt another message?(y/n)')
    again = input().lower()
