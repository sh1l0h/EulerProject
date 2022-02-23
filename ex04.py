import math

def isPalindrome(num):
    st = str(num)
    if len(st) == 0 or len(st) == 1:
        return True
    first = st[0]
    last = st[len(st)-1]
    mid = st[1:len(st)-1]
    return last == first and isPalindrome(mid)


def isMul(num):
    for i in range(100, 1000):
        if num % i == 0 and int(math.floor(math.log(num/i,10))) == 2:
            return True
    return False
    
num = 999*999 
while True:
    if isPalindrome(num) and isMul(num):
        print(num)
        break
    num -= 1
