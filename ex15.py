dic = {}
def solution(x,y):
    if x == 1 or y == 1:
        return x*y + 1
    if (x, y) in dic:
        return dic[(x,y)]
    if not (x-1, y) in dic:
        dic[(x-1,y)] = solution(x - 1,y)
    if not (x,y-1) in dic:
        dic[(x,y-1)] = solution(x, y-1)
    tmp = dic[(x,y-1)] + dic[(x-1,y)]
    dic[(x,y)] = tmp 
    return tmp 

print(solution(20,20))
