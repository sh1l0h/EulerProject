# With pre-generated prime numbers this program would be way faster, but I'm too lazy to download the file.

import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False;
    return True

def getFactorNum(num):
    factors = []
    while num > 1:
        if num % 2 == 0:
            factors.append(2)
            num /= 2
            continue
        
        prime = 3
        while not isPrime(prime) or num % prime != 0:
            prime += 2
        factors.append(prime)
        num = num / prime
    dic = dict((x, factors.count(x)) for x in set(factors))
    result = 1
    for e in dic:
        result *= 1 + dic[e]
    return result
        
last = 1
curr = 3
while True:
    if getFactorNum(last) > 500:
        print(last)
        break
    temp = curr - last
    last = curr
    curr += temp + 1
        
    
