num = 3
dic = {2: 1,
       1: 0}
stack = []
theNum = 0
maxNum = 0
while num < 1000000:
    tmp = num
    while True:
        if tmp in dic:
            if not stack:
                break
            dic[stack[-1]]=1 + dic[tmp] 
            break
        stack.append(int(tmp))
        if tmp % 2 != 0:
            tmp = 3*tmp +1
        else:
            tmp /= 2
    if stack:
        last = stack.pop()
        while stack:
            curr = stack.pop()
            dic[curr] = 1 + dic[last]
            last = curr
    if dic[num] > maxNum:
        theNum = num
        maxNum = dic[num]
    num += 1
print(theNum)
