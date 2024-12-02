import sys
D = open(sys.argv[1]).read().strip()

expectedScore = 0

digits = []

def toNumber(character):
    if (character == "A") or (character == "X"):
        return 1
    if (character == "B") or (character == "Y"):
        return 2
    if (character == "C") or (character == "Z"):
        return 3
    return 0


for line in D.splitlines():
    moves = line.split()
    myMove = 9
    hisMove = toNumber(moves[0])
    gameGoal = toNumber(moves[1])
    if (gameGoal == 1):
        myMove = hisMove - 1
        if (myMove == 0):
            myMove = 3
    if (gameGoal == 2):
        expectedScore += 3
        myMove = hisMove
    if (gameGoal == 3):
        expectedScore += 6
        myMove = hisMove + 1
        if (myMove == 4):
            myMove = 1
    expectedScore += myMove


print(expectedScore)
