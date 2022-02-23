import math

def isSquare(num : int):
    temp = int(math.sqrt(num))
    return temp**2 == num

limit = 1000
for i in range(1,limit):
    for j in range(i,limit):
        c = i**2 + j**2
        if isSquare(c) and math.sqrt(c) + i + j == 1000:
            print(math.sqrt(c)*j*i)
            exit(0)
