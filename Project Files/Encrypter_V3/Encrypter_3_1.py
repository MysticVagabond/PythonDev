import random
class encryptSentenceClass:
    def encrypt(self, sentence):
        self.origText = sentence
        self.origList = sentence.split()
        wordLi_V1 = self.createWordLi_V1(sentence)#after the words have been scrambled
        lenAndIndex_V1 = self.getLengthsAndIndexes(wordLi_V1)
        key = random.randint(2,25)
        wordLi_V2 = []
        for word in wordLi_V1:
            if word.startswith('|'):
                wordLi_V2.append(word)
            else:
                wordLi_V2.append(self.shiftLettersByKey(word, key))
        combinedList = self.combineWordsAndNums(wordLi_V2, lenAndIndex_V1)
        finalResult = self.mergeWordsIntoContinuousString(combinedList, key)
        return (finalResult)
                                 
    def mergeWordsIntoContinuousString(self, wordLi, key):
        if key < 10:
            finalString = '0' + str(key)
        else: finalString = str(key)
        random.shuffle(wordLi)
        for word in wordLi:
            finalString += str(word)
        return (finalString)

    def combineWordsAndNums(self, wordLi, numLi):
        combinedLi = []
        for i in range(len(wordLi)):
            tempStr = ''
            if wordLi[i].startswith('|'):   #uses the pipe to show it is a number that the user wrote
                tempStr = wordLi[i] + numLi[i]
            else:
                if len(wordLi[i]) > len(numLi[i]):
                    longest = len(wordLi[i])
                else: longest = len(numLi[i])
                for j in range(longest):
                    try:
                        tempStr += wordLi[i][j]
                    except IndexError:
                        pass
                    try:
                        tempStr += numLi[i][j]
                    except IndexError:
                        pass
            combinedLi.append(tempStr)
        return (combinedLi)
        
    def shiftLettersByKey(self, word, key):
        newWord = ''
        for letter in word:
            num = ord(letter)
            if ((65 <= num <= 90) or (97 <= num <= 122)): 
                num += key
                if letter.isupper():
                    if num > ord('Z'):
                        num -= 26
                elif letter.islower():
                    if num > ord('z'):
                        num -= 26
            newWord += chr(num)
        reverseWord = self.reverseOrder(newWord)
        return (reverseWord)

    def getLengthsAndIndexes(self, wordLi_V1):
        numLi = []
        for tempIndex in range(len(wordLi_V1)):
            tempLen = len(wordLi_V1[tempIndex])
            if tempLen < 10:
                tempLenStr = '0' + str(tempLen)
            else:
                tempLenStr = str(tempLen)
            if tempIndex < 10:
                tempIndexStr = '00' + str(tempIndex)
            elif tempIndex < 100:
                tempIndexStr = '0' + str(tempIndex)
            else:
                tempIndexStr = str(tempIndex)

            numLi.append(tempLenStr+tempIndexStr)
        return (numLi)

    def createWordLi_V1(self, sentence):
        tempWordList = []
        for word in sentence.split():
            if word.isdigit():
                tempWordList.append(self.encryptNumberWithinText(int(word)))
            else:
                tempWordLen = len(word)
                if tempWordLen == 1:
                    tempWordList.append(word)
                elif tempWordLen == 2:
                    word = word[::-1]
                    tempWordList.append(word)
                elif tempWordLen % 3 == 0:
                    tempWordList.append(self.threeLetterMultiple(word))
                elif tempWordLen % 4 == 0:
                    tempWordList.append(self.fourLetterMultiple(word))
                elif tempWordLen % 5 == 0:
                    tempWordList.append(self.fiveLetterMultiple(word))
                elif tempWordLen % 7 == 0:
                    tempWordList.append(self.sevenLetterMultiple(word))
                elif tempWordLen in [11,13,17,19,23,29]:
                    tempWordList.append(self.longPrimeNumbers(word))
                else:
                    print(word.ljust(40, '-') + 'Not Translated')
                    tempWordList.append(word)
        return (tempWordList)

    def encryptNumberWithinText(self, num):
        newNumStr = '|'
        intNum = num**2
        strNum = str(intNum)
        for i in range(len(strNum)):
            randNum = random.randint(1,9)
            newNumStr += str(randNum) + strNum[i]
        newNumStr += '|'
        reverseNewNumStr = self.reverseOrder(newNumStr)
        return (reverseNewNumStr)
    
    def threeLetterMultiple(self, word):    #the eth
        newWord = ''
        for sectNum in range(int(len(word)/3)):
            newWord += word[2+(sectNum*3)]
            newWord += word[0+(sectNum*3)]
            newWord += word[1+(sectNum*3)]
        return (newWord)
    
    def fourLetterMultiple(self, word):    #four rfuo
        newWord = ''
        for sectNum in range(int(len(word)/4)):
            newWord += word[3+(sectNum*4)]
            newWord += word[0+(sectNum*4)]
            newWord += word[2+(sectNum*4)]
            newWord += word[1+(sectNum*4)]
        return (newWord)
    
    def fiveLetterMultiple(self, word):    #fiver vrfei
        newWord = ''
        for sectNum in range(int(len(word)/5)):
            newWord += word[2+(sectNum*5)]
            newWord += word[4+(sectNum*5)]
            newWord += word[0+(sectNum*5)]
            newWord += word[3+(sectNum*5)]
            newWord += word[1+(sectNum*5)]
        return (newWord)
    
    def sevenLetterMultiple(self, word):    #program oprmgar
        newWord = ''
        for sectNum in range(int(len(word)/7)):
            newWord += self.threeLetterMultiple(word[sectNum*7:(sectNum*7)+3:])
            newWord += self.fourLetterMultiple(word[(sectNum*7)+3:(sectNum*7)+7:])
        return (newWord)
    
    def longPrimeNumbers(self, word):
        newWord = ''
        for i in range(int(len(word) // 5)):   #splits the string into sets of 5 and then deals with the remainder
            newWord += self.fiveLetterMultiple(word[0:5])
            word = word[5:]
        if len(word) == 1:
            newWord += word
        elif len(word) == 2:
            newWord += word[::-1]
        elif len(word) == 3:
            newWord += self.threeLetterMultiple(word)
        elif len(word) == 4:
            newWord += self.fourLetterMultiple(word)
        return (newWord)

    def reverseOrder(self, string):
        return (string[::-1])    #reverses the order of the string



if __name__ == '__main__':
    
    Encrypter = encryptSentenceClass()#initialise the class to be able to access its functions
    sentence = input('Type sentence/word to encrypt: ')
    sentence = Encrypter.encrypt(sentence)
    print(sentence,'\nDone')

#Hello my name is stephen
#07h0t4u0l02o0l7w0u0a4zlt0f2001l0s5O0v0s0p0z2003


