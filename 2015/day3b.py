import sys
file = open(sys.argv[1]).read().strip()

# print(file)

santaX = 0
santaY = 0
robotX = 0
robotY = 0
housesWithPresent = []
santa = ""
robot = ""

i = 0
for arrow in file:
    i += 1
    if (i % 2 == 0):
        santa += arrow
    else:
        robot += arrow


for arrow in santa:
    housesWithPresent.append([santaX,santaY])
    if (arrow == "^"):
        santaY += 1
    if (arrow == "v"):
        santaY -= 1
    if (arrow == "<"):
        santaX -= 1
    if (arrow == ">"):
        santaX += 1
    locationTuple = (santaX, santaY)
    housesWithPresent.append(locationTuple)

for arrow in robot:
    housesWithPresent.append([santaX,santaY])
    if (arrow == "^"):
        robotY += 1
    if (arrow == "v"):
        robotY -= 1
    if (arrow == "<"):
        robotX -= 1
    if (arrow == ">"):
        robotX += 1
    locationTuple = (robotX, robotY)
    housesWithPresent.append(locationTuple)

ans = set(tuple(element) for element in housesWithPresent)
print(len(ans))
