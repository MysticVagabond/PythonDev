import random

def createName(name, key):
    newName = ''
    for letter in name:
        num = ord(letter)
        num += key
        if letter.isupper():
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
        elif letter.islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
        newName += chr(num)
    reverseName = reverseOrder(newName)
    return reverseName
    
def createNumber(number):
    encValue = ''
    newNum = number * number
    stringNum = str(newNum)
    for i in range(len(stringNum)):
        randNum = random.randint(1,9)
        encValue += str(randNum) + stringNum[i]
    reverseString = reverseOrder(encValue)
    return reverseString

def mergeNumAndString(name, num, key):
    if key < 10:
        strKey = '0' + str(key)
    else: strKey = str(key)

    if len(name) > len(num):
        longest = len(name)
    else: longest = len(num)

    wholeString = strKey
    for i in range(longest):
        try:
            wholeString += name[i]
        except IndexError:
            pass
        try:
            wholeString += num[i]
        except IndexError:
            pass
    return wholeString

def reverseOrder(string):
    reverse = ''
    for i in range(len(string)):
        x = (len(string) - 1) - i
        reverse += string[x]
    return reverse
    
if __name__ == '__main__':
    userName = 'Roberto'
    encryptKey = 12
    userScore = 100

    print(createName("ABCD", 2))
        
    encodedName = createName(userName, encryptKey)
    encodedNum = createNumber(userScore)
    wholeEncryptedString = mergeNumAndString(encodedName, encodedNum, encryptKey)
    print('Name: %s, Number: %s, Encryption: %s' % (encodedName, encodedNum, wholeEncryptedString))



















