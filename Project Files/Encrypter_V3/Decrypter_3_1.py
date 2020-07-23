import math
class decryptSentenceClass:
    def decrypt(self, sentence):
        wordStr, numStr = self.separateWordsAndNumbers(sentence)
        
        key, lenAndIndex_V1 = self.getLengthsAndIndexes(numStr)
        
        wordLi_V2 = ['']*len(lenAndIndex_V1)
        wordLi_V2 = self.separateWordString(wordStr, lenAndIndex_V1, wordLi_V2)
        wordLi_V1 = []
        for word in wordLi_V2:
            if word.startswith('|'):
                wordLi_V1.append(word)
            else:
                wordLi_V1.append(self.shiftLettersByKey(word, key))
        origSentance = self.createWordsFromWordLi_V1(wordLi_V1)
        return origSentance

        
    def separateWordString(self, wordStr, lenAndIndex_V1, wordLi_V2):
        for section in lenAndIndex_V1:
            wordLi_V2[section[1]] = wordStr[:section[0]]
            wordStr = wordStr[section[0]:]
        return (wordLi_V2)

    def separateWordsAndNumbers(self, contString):
        wordStr = ''
        numStr = ''
        userNum = False
        for letter in range(len(contString)):
            tempLetter = contString[:1]
            if tempLetter == '|':#if a pipe it adds to the wordStr then nots the bool value
                userNum = not(userNum)
                wordStr += tempLetter
                
            elif tempLetter.isdigit() and userNum:#if the user has typed the number
                wordStr += tempLetter
            elif tempLetter.isdigit() and not(userNum):#if it is a generic number
                numStr += tempLetter
            else: wordStr += tempLetter
            contString = contString[1:]
        return (wordStr, numStr)
                
    def shiftLettersByKey(self, word, key):
        oldWord = ''
        for letter in word:
            num = ord(letter)
            if ((65 <= num <= 90) or (97 <= num <= 122)): 
                num -= key
                if letter.isupper():
                    if num < ord('A'):
                        num += 26
                elif letter.islower():
                    if num < ord('a'):
                        num += 26
            oldWord += chr(num)
        reverseOldWord = self.reverseOrder(oldWord)
        return (reverseOldWord)

    def getLengthsAndIndexes(self, numStr):
        lenIndexLi = []
        key = numStr[:2]
        numStr = numStr[2:]
        for i in range(int(len(numStr)/5)):
            length = numStr[:2]
            index = numStr[2:5]
            lenIndexLi.append([int(length), int(index)])
            numStr = numStr[5:]
        return (int(key), lenIndexLi)

    def createWordsFromWordLi_V1(self, wordLi):
        sentence = ''
        for word in wordLi:
            if word.startswith('|'):
                sentence += str(self.decryptNumberWithinText(word))
            else:
                tempWordLen = len(word)
                if tempWordLen == 1:
                    sentence += word
                elif tempWordLen == 2:
                    word = word[::-1]
                    sentence += word
                elif tempWordLen % 3 == 0:
                    sentence += self.threeLetterMultiple(word)
                elif tempWordLen % 4 == 0:
                    sentence += self.fourLetterMultiple(word)
                elif tempWordLen % 5 == 0:
                    sentence += self.fiveLetterMultiple(word)
                elif tempWordLen % 7 == 0:
                    sentence += self.sevenLetterMultiple(word)
                elif tempWordLen in [11,13,17,19,23,29]:
                    sentence += self.longPrimeNumbers(word)
            sentence += ' '
        return (sentence)

    def decryptNumberWithinText(self, num):
        num = num[1:len(num)-1:]
        oldNumStr = self.reverseOrder(num)
        oldNum = ''
        for i in range(len(oldNumStr)):
            if i % 2 == 1:
                oldNum += oldNumStr[i]

        oldNum = int(math.sqrt(int(oldNum)))
        return (oldNum)

    def threeLetterMultiple(self, word):   #eth the
        oldWord = ''
        for sectNum in range(int(len(word)/3)):
            oldWord += word[1+(sectNum*3)]
            oldWord += word[2+(sectNum*3)]
            oldWord += word[0+(sectNum*3)]
        return (oldWord)

    def fourLetterMultiple(self, word):    #rfuo four
        oldWord = ''
        for sectNum in range(int(len(word)/4)):
            oldWord += word[1+(sectNum*4)]
            oldWord += word[3+(sectNum*4)]
            oldWord += word[2+(sectNum*4)]
            oldWord += word[0+(sectNum*4)]
        return (oldWord)

    def fiveLetterMultiple(self, word):    #vrfei fiver
        oldWord = ''
        for sectNum in range(int(len(word)/5)):
            oldWord += word[2+(sectNum*5)]
            oldWord += word[4+(sectNum*5)]
            oldWord += word[0+(sectNum*5)]
            oldWord += word[3+(sectNum*5)]
            oldWord += word[1+(sectNum*5)]
        return (oldWord)

    def sevenLetterMultiple(self, word):    #program oprmgar
        oldWord = ''
        for sectNum in range(int(len(word)/7)):
            oldWord += self.threeLetterMultiple(word[sectNum*7:(sectNum*7)+3:])
            oldWord += self.fourLetterMultiple(word[(sectNum*7)+3:(sectNum*7)+7:])
        return (oldWord)
    
    def longPrimeNumbers(self, word):
        oldWord = ''
        for i in range(int(len(word) // 5)):   #splits the string into sets of 5 and then deals with the remainder
            oldWord += self.fiveLetterMultiple(word[0:5])
            word = word[5:]
        if len(word) == 1:
            oldWord += word
        elif len(word) == 2:
            oldWord += word[::-1]
        elif len(word) == 3:
            oldWord += self.threeLetterMultiple(word)
        elif len(word) == 4:
            oldWord += self.fourLetterMultiple(word)
        return (oldWord)

    def reverseOrder(self, string):
        return (string[::-1])    #reverses the order of the string

if __name__ == '__main__':
    
    Decrypter = decryptSentenceClass()#initialise the class to be able to access its functions  wordStr, numStr = Decrypter.separateWordsAndNumbers('05j0q5m0t0q0')
    sentence = input('Type sentence/word to decrypt: ')
    sentence = Decrypter.decrypt(sentence)
    print(sentence,'\nDone')
    
