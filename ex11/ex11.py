
f = open("grid.txt", "r")
lines = f.readlines()

grid = []
for l in lines:
    row = l.split(' ')
    grid.append(list(map(int, row)))

f.close()

adjacentNums = 4
result = -1
for row in range(len(grid)):
    for column in range(len(grid[row])):
        currMax = -1
        if len(grid[row]) - column >= adjacentNums:
            tmp = 1
            for i in range(adjacentNums):
                tmp *= grid[row][column + i]
            currMax = tmp 
        if len(grid) - row >= adjacentNums:
            tmp = 1
            for i in range(adjacentNums):
                tmp *= grid[row+i][column]
            if tmp > currMax:
                currMax = tmp
        if min(len(grid) - row, len(grid[row]) - column) >= adjacentNums:
            tmp = 1
            for i in range(adjacentNums):
                tmp *= grid[row+i][column+i]
            if tmp > currMax:
                currMax = tmp
        if min(len(grid) - row, 1 + column) >= adjacentNums:
            tmp = 1
            for i in range(adjacentNums):
                tmp *= grid[row+i][column-i]
            if tmp > currMax:
                currMax = tmp
        if currMax > result:
            result = currMax
print(result)
