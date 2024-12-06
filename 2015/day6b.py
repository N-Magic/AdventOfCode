import sys

file = open(sys.argv[1]).read().strip()

grid = [[0] * 1000 for _ in range(1000)]
# print(grid)
def on(x1,y1,x2,y2):
    x2 += 1
    y2 += 1
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] += 1
def off(x1,y1,x2,y2):
    x2 += 1
    y2 += 1
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] -= 1
            if (grid[i][j] < 0):
                grid[i][j] = 0
def toggle(x1,y1,x2,y2):
    x2 += 1
    y2 += 1
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] += 2

for guide in file.splitlines():
    guide = guide.split()
    mode = ""
    values = []
    if (guide[1] == "on"):
        mode = "on"
        values = guide[2:]
    elif (guide[1] == "off"):
        mode = "off"
        values = guide[2:]
    else:
        mode = "toggle"
        values = guide[1:]
    # print(mode)
    # print(values)
    firstPair = values[0]
    secondPair = values[2]
    firstPair = firstPair.split(",")
    secondPair = secondPair.split(",")
    if (mode == "on"):
        on(int(firstPair[0]), int(firstPair[1]), int(secondPair[0]), int(secondPair[1]))
    if (mode == "off"):
        off(int(firstPair[0]), int(firstPair[1]), int(secondPair[0]), int(secondPair[1]))
    if (mode == "toggle"):
        toggle(int(firstPair[0]), int(firstPair[1]), int(secondPair[0]), int(secondPair[1]))
ans = 0
for i in range(1000):
    for j in range(1000):
        ans += grid[i][j]
print(ans)
