import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False;
    return True

n = 600851475143
max = 0
for i in range(1, int(math.sqrt(n))):
   if n % i == 0:
       if isPrime(i) and i > max:
           max = i
       if isPrime(n/i) and n/i > max:
           max = n/i
print(max)
           
    
