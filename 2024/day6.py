import sys
import time

file = open(sys.argv[1]).read().strip()

grid = []
for thing in file.splitlines():
    line = []
    for char in thing:
        line.append(char)
    grid.append(line)
# print(grid)

# 0 means rotated, 1 means moved, 2 means it ran into an x and is done

def nicePrint(grid):
    for line in grid:
        print(line)

def updateGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == "."):
                continue
            if (grid[i][j] == ("^")):
                if (i - 1 < 0):
                    return 999
                if (i - 1 < 0) or (grid[i-1][j] == "#"):
                    grid[i][j] = ">"
                    return 0
                # elif (grid[i-1][j] == "X"):
                #     grid[i][j] = "X"
                #     return 2
                else:
                    grid[i][j] = "X"
                    grid[i-1][j] = "^"
                    return 1
            if (grid[i][j] == (">")):
                if (j + 1 == len(grid[0])):
                    return 999
                if (j + 1 == len(grid[0])) or (grid[i][j + 1] == "#"):
                    grid[i][j] = "v"
                    return 0
                # elif (grid[i][j + 1] == "X"):
                #     grid[i][j] = "X"
                #     return 2
                else:
                    grid[i][j] = "X"
                    grid[i][j + 1] = ">"
                    return 1
            if (grid[i][j] == ("v")):
                if (i + 1 == len(grid)):
                    return 999
                if (i + 1 == len(grid)) or (grid[i+1][j] == "#"):
                    grid[i][j] = "<"
                    return 0
                # elif (grid[i+1][j] == "X"):
                #     grid[i][j] = "X"
                #     return 2
                else:
                    grid[i][j] = "X"
                    grid[i+1][j] = "v"
                    return 1
            if (grid[i][j] == ("<")):
                if (j - 1 < 0):
                    return 999
                if (j - 1 < 0) or (grid[i][j -1] == "#"):
                    grid[i][j] = "^"
                    return 0
                # elif (grid[i][j-1] == "X"):
                #     grid[i][j] = "X"
                #     return 2
                else:
                    grid[i][j] = "X"
                    grid[i][j-1] = "<"
                    return 1

def countX(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == "X"):
                ans += 1
    return(ans)

currentProgress = 0
while (currentProgress == 0) or (currentProgress == 1):
    currentProgress = updateGrid(grid)
print(currentProgress)

print(countX(grid) + 1)
