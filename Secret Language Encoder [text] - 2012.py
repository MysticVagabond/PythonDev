#Secret language program / Stephen Fisher / 10 Jan 2012

def decodeMessage(letter, code, secretAlphabet, Alphabet):
    if letter in secretAlphabet:
        n = secretAlphabet.index(letter)
        n -= code
        if n < 0:
            n += 26#because you subtract the code the letter may be below 26 so it adds 26 
        return Alphabet[n]
    elif letter == '_':
        return ' '
    else:
        return letter
def encodeMessage(letter, code, secretAlphabet, Alphabet):
    if letter in Alphabet:
        n = Alphabet.index(letter)
        n += code
        if n >= 26:#because you add the code the letter may be above 26 so it removes 26 
            n -= 26
        return secretAlphabet[n]
    elif letter == ' ':
        return '_'
    else:
        return letter
def again():#obvious
    print('Do you want to Decode or Encode another message? (yes or no)')
    return input().lower().startswith('y')

Alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()#alphabets for it to index
secretAlphabet = '@ |} { |] £ |= &, |-| ; .¬ |< | ^^ |¬ 0 |* *| ,~ $ +- v, \/ \/\/ >< ^| %'.split()
while True:
    print('Welcome')
    getCode = True
    while getCode == True:
        choice = input('Decode or Encode?\n').lower()
        if choice in 'decode d encode e'.split():
            codeUsed = input('Code used(y/n)?\n').lower().startswith('y')
            if codeUsed == True:
                code = int(input('Num(0-26)?\n'))#the code is an encryption key that confuses the reader
            else:
                code = 0
            getCode = False
        elif choice in 'brute b'.split():
            getCode = False
        else:
            print('Not a valid choice choose again!')
    messageIN = input('Type Message...\n').lower()
    if choice in 'decode d'.split():#decode bit
        transMessage = ''
        message = messageIN.split()#splits the message into a list of each character
        for i in range(0,len(message)):
            message[i] = decodeMessage(message[i], code, secretAlphabet, Alphabet)
            transMessage += message[i]
        print('Your Message:\n',transMessage)
    elif choice in 'encode e'.split():#encode bit
        transMessage = []
        lastMessage = ''
        message = list(messageIN)
        for i in range(0,len(message)):
            transMessage.append(encodeMessage(message[i], code, secretAlphabet, Alphabet))
            lastMessage += str(transMessage[i]) + ' '
        print('Your Message:\n', lastMessage)
    elif choice in 'brute b'.split():#brute force bit that uses each code num to crack the encryption
        for x in range(26):
            code = int(x)
            transMessage = []
            lastMessage = ''
            message = messageIN.split()
            for i in range(0,len(message)):
                transMessage.append(decodeMessage(message[i], code, secretAlphabet, Alphabet))
                lastMessage += transMessage[i]
            print('Your Message:', x, lastMessage)
    if not again():
        break
