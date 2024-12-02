import sys
# import math
source = open(sys.argv[1]).read().strip()
leftList = []
rightList = []
distance = 0

for line in source.splitlines():
    words = line.split()
    leftList.append(words[0])
    rightList.append(words[1])
leftList.sort()
rightList.sort()
for i in range(0, len(leftList)):
    individualDistance = int(leftList[i]) - int(rightList[i])
    distance += abs(individualDistance)
print(distance)
