import sys
D = open(sys.argv[1]).read().strip()

expectedScore = 0

digits = []

def toNumber(character):
    if (character == "A") or (character == "X"):
        return 0
    if (character == "B") or (character == "Y"):
        return 1
    if (character == "C") or (character == "Z"):
        return 2
    return 0


for line in D.splitlines():
    moves = line.split()
    if (toNumber(moves[0]) == toNumber(moves[1]) - 1) or (toNumber(moves[0]) == toNumber(moves[1]) + 2):
        expectedScore += 6
    elif (toNumber(moves[0]) == toNumber(moves[1])):
        expectedScore += 3
    expectedScore += toNumber(moves[1]) + 1
print(expectedScore)
