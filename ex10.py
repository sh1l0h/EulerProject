import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False;
    return True

result = 2
num = 3
while num < 2000000:
    if isPrime(num):
        result += num
    num += 2

print(result)
