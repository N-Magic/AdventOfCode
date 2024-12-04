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
        if (twodarray[i][j] == "X"):
            if (j + 3 < len(twodarray[0])): #checking things to it's right
                if (twodarray[i][j+1] == "M") and (twodarray[i][j+2] == "A") and (twodarray[i][j+3] == "S"):
                    christmas += 1
                if (i + 3 < len(twodarray)):
                    if (twodarray[i+1][j+1] == "M") and (twodarray[i+2][j+2] == "A") and (twodarray[i+3][j+3] == "S"):
                        christmas += 1
                if (i - 3 >= 0):
                    if (twodarray[i-1][j+1] == "M") and (twodarray[i-2][j+2] == "A") and (twodarray[i-3][j+3] == "S"):
                        christmas += 1
            if (i + 3 < len(twodarray)):
                if (twodarray[i+1][j] == "M") and (twodarray[i+2][j] == "A") and (twodarray[i+3][j] == "S"):
                    christmas += 1
            if (i - 3 >= 0):
                if (twodarray[i-1][j] == "M") and (twodarray[i-2][j] == "A") and (twodarray[i-3][j] == "S"):
                    christmas += 1
            # to the left
            if (j - 3 >= 0):
                if (twodarray[i][j-1] == "M") and (twodarray[i][j-2] == "A") and (twodarray[i][j-3] == "S"):
                    christmas += 1
                if (i + 3 < len(twodarray)):
                    if (twodarray[i+1][j-1] == "M") and (twodarray[i+2][j-2] == "A") and (twodarray[i+3][j-3] == "S"):
                        christmas += 1
                if (i - 3 >= 0):
                    if (twodarray[i-1][j-1] == "M") and (twodarray[i-2][j-2] == "A") and (twodarray[i-3][j-3] == "S"):
                        christmas += 1
print(christmas)
