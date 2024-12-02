import sys
file = open(sys.argv[1]).read().strip()

print(file)

santaX = 0
santaY = 0
housesWithPresent = []

for arrow in file:


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
ans = set(tuple(element) for element in housesWithPresent)
print(len(ans))
