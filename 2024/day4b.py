import sys

file = open(sys.argv[1]).read().strip()

twodarray = []

for line in file.splitlines():
    lineArray = []
    for char in line:
        lineArray.append(char)
    twodarray.append(lineArray)

christmas = 0

for i in range(len(twodarray)):
    for j in range(len(twodarray[0])):
        if (i != 0) and (j != 0) and (i + 1 < len(twodarray)) and (j + 1 < len(twodarray[0])) and (twodarray[i][j] == "A"):
            masses = 0
            if (twodarray[i-1][j-1] == "M") and (twodarray[i+1][j+1] == "S"):
                masses += 1
            if (twodarray[i+1][j-1] == "M") and (twodarray[i-1][j+1] == "S"):
                masses += 1
            if (twodarray[i-1][j+1] == "M") and (twodarray[i+1][j-1] == "S"):
                masses += 1
            if (twodarray[i+1][j+1] == "M") and (twodarray[i-1][j-1] == "S"):
                masses += 1
            if (masses == 2):
                christmas += 1
print(christmas)
