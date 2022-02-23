import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False;
    return True

index = 0
num = 2
while True:
    if isPrime(num):
        index += 1
        if index == 10001:
            print(num)
            break
    num += 1
