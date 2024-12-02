import sys
D = open(sys.argv[1]).read().strip()
highestCal = 0
highestCal2 = 0
highestCal3 = 0
currentCal = 0
digits = []
for line in D.splitlines():
    if (line != ""):
        currentCal += int(line)
        if (highestCal < currentCal):
            highestCal3 = highestCal2
            highestCal2 = highestCal
            highestCal = currentCal
        elif (highestCal2 < currentCal):
            highestCal3 = highestCal2
            highestCal2 = currentCal
        elif (highestCal3 < currentCal):
            highestCal3 = currentCal
    if (line == ""):
        currentCal = 0
print(highestCal)
print(highestCal2)
print(highestCal3)
print(highestCal + highestCal2 + highestCal3)
