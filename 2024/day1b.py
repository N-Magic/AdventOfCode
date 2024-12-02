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
for left in leftList:
    wordSimilarity = 0
    for right in rightList:
        if (int(left) == int(right)):
            wordSimilarity += int(left)
    distance += wordSimilarity
print(distance)
