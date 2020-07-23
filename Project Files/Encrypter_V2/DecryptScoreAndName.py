import math

def getName(origName, key):
    name = ''
    key = -int(key)
    for letter in origName:
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
        name += chr(num)
    name = reverseOrder(name)
    return name

def getNumber(num):
    num = reverseOrder(num)
    unencryptedValue = ""
    for i in range(len(num)):
        if i % 2 == 1:
            unencryptedValue += num[i]

    value = int(math.sqrt(int(unencryptedValue)))
    return value

def reverseOrder(string):
    reverse = ''
    for i in range(len(string)):
        x = (len(string) - 1) - i
        reverse += string[x]
    return reverse

def unmergeNumAndString(userInput):
    name = ''
    num = ''

    for i in range(len(userInput)):
        if userInput[i].isalpha():
            name += userInput[i]
        else: num += userInput[i]
    return [name, num]

if __name__ == '__main__':
    userInput = '12z0q2t0b7q0f8E0616'
    key = userInput[:2]
    origName = userInput[2:]
    print('Key: %s, Encryption: %s' % (key, origName))
    name, number = unmergeNumAndString(origName)
    print('Separated Name: %s, Separated Number: %s' % (name, number))
    correctName = getName(name, key)
    correctScore = getNumber(number)
    print('Decrypted Name: %s, Decrypted Score: %s' % (correctName, correctScore))
























