# import random
import sys
# from itertools import permutations

file = open(sys.argv[1]).read().strip()

orderRules = []
updatePages = []

answer = 0
onesToProcess = 0

orderingRules = True

def sortDat(input):
    working = input[:]
    while True:
        changed = False
        for rule in orderRules:
            if rule[0] in working and rule[1] in working:
                index0 = working.index(rule[0])
                index1 = working.index(rule[1])
                if index0 > index1:
                    working[index0], working[index1] = working[index1], working[index0]
                    changed = True
        if not changed:
            break

    return working
for line in file.splitlines():
    if orderingRules:
        if (line == ""):
            orderingRules = False
            continue
        else:
            orderRules.append([line.split("|")[0], line.split("|")[1]])
    else:
        updatePages.append(line.split(","))

missOrdered = []

for pages in updatePages:
    setIsGood = True
    for i in range(len(pages) - 1):
        twoPagesGood = False
        for orderRule in orderRules:
            if (pages[i] == orderRule[0]) and (pages[i+1] == orderRule[1]):
                twoPagesGood = True
        if not twoPagesGood:
            setIsGood = False
    if setIsGood:
        answer += int(pages[int((len(pages) - 1) / 2)])
    else:
        missOrdered.append(pages)
secondAnswer = 0
for wrong in missOrdered:
    sortedArray = sortDat(wrong)
    secondAnswer += int(sortedArray[int((len(sortedArray) - 1) / 2)])
print(secondAnswer)
