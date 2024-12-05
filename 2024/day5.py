
import sys

file = open(sys.argv[1]).read().strip()

orderRules = []
updatePages = []

answer = 0

orderingRules = True

for line in file.splitlines():
    if orderingRules:
        if (line == ""):
            orderingRules = False
            continue
        else:
            orderRules.append([line.split("|")[0], line.split("|")[1]])
    else:
        updatePages.append(line.split(","))
print(updatePages)

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
print(answer)
