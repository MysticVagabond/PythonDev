import random, math

value = 372
print('Value: ' + str(value))
newValue = value * value
stringValue = str(newValue)

encryptedValue = ""
for i in range(len(stringValue)):
    randNum = random.randint(0,9)
    encryptedValue += str(randNum) + stringValue[i]


reverseEncValue = ""
for i in range(len(encryptedValue)):
    x = len(encryptedValue) - i - 1
    reverseEncValue += encryptedValue[x]
print('Encrypted value: ' + reverseEncValue)


convertValue = reverseEncValue
unreverseEncValue = ""
for i in range(len(convertValue)):
    x = len(convertValue) - i - 1
    unreverseEncValue += convertValue[x]
    
unencryptedValue = ""
for i in range(len(unreverseEncValue)):
    if i % 2 == 1:
        unencryptedValue += unreverseEncValue[i]

unValue = int(math.sqrt(int(unencryptedValue)))

print('Unencrypted Value: ' + str(unValue))
