num = 2*3*7*11*5*19*2*3*13*17
while True:
    found = True
    for i in range(2,21):
        if num % i != 0:
            found = False
            break
    if found:
        print(num)
        break
    else:
        num += 10
        
