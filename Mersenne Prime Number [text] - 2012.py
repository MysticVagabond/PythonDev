import math
def isPrime(num):
    sqrt = math.sqrt(num)
    i = 2
    prime = True
    while i <= sqrt:
        if num % i == 0:
            prime = False
        i += 1
    return prime
def isMersennePrime(num):
    if isPrime(num):
        print('Is Prime...')
        mersenneNum = (2**num) - 1
        #print(mersenneNum)
        if isPrime(mersenneNum):
            print('Is Mersenne Prime.')
        else: print('Is NOT Mersenne Prime.')
    else: print('NOT Prime, therefore NOT Mersenne prime.')
num = int(input('Type the Number to check if a Mersenne prime:\n'))
isMersennePrime(num)
    

