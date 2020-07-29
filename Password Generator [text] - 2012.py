import random
Alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
passwords = []
duplicates = 0
numPass = int(input('How many Passwords?'))
numCode = int(input('How many characters?'))
for i in range(numPass):
    currPass = ''
    for j in range(numCode):
        digitType = random.randint(0,1)
        if digitType == 0:
            currDigit = random.randint(0,9)
        elif digitType == 1:
            currDigit = Alphabet[random.randint(0,25)]
        currPass += str(currDigit)
        
    if currPass in passwords:
        i -= 1
        duplicates += 1
    else:
        passwords.append(currPass)
        print(str(i +1) + '. ' + currPass)
print(duplicates, 'duplicates were created and removed')
input()

