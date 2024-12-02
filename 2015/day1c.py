import sys
file = open(sys.argv[1]).read().strip()
floors = 0
intoTheBasement = 0
for i, char in enumerate(file):
    if (char == "("):
        floors += 1
    if (char == ")"):
        floors -= 1
        if (floors == -1) and (intoTheBasement == 0):
            intoTheBasement = i + 1
print(floors)
print(intoTheBasement)
