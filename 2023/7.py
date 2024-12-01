import sys
total = 0
games = open(sys.argv[1]).read().splitlines()
values = []


for game in games:
    bet = game.split(" ")[1]
    hand = game.split(" ")[0]
    # print(bet,hand)
    cards = []
    for num in hand:
        if num == "A":
            cards.append(14)
        elif num == "K":
            cards.append(13)
        elif num == "Q":
            cards.append(12)
        elif num == "J":
            cards.append(11)
        elif num == "T":
            cards.append(10)
        else:
            cards.append(int(num))
    print(cards)
    numberOfMatches = 0
    tempMatches = 0
    highestNumber = 0


    for i, card in enumerate(cards):
        j = 0
        matchedIndex = 0
        tempMatches = 0
        while j < 5:
            if card > highestNumber:
                highestNumber = card
            if card == cards[j] and i != j:
                tempMatches +=1
                if tempMatches > numberOfMatches:
                    numberOfMatches = tempMatches
                    matchedIndex = i
            j += 1
    determineFullHouse = 6
    fullHouse = False
    print(numberOfMatches)
    if numberOfMatches == 2:
        for i, card in enumerate(cards):
            if card != cards[matchedIndex]:
                if card == determineFullHouse:
                    fullHouse = True
                determineFullHouse = i
            
#  Single = 1, Double = 2, Triple = 3, FullHouse = 4, Quad = 5, 5 = 6
    if fullHouse == True:
        values.append([matchedIndex+2, cards[matchedIndex], cards])
    else:
        values.append([matchedIndex+1, cards[matchedIndex], cards])
    # Format is match type, matched value, arrray of cards

highestGrouping = 0
highestCard = 0

for value in values:
    if value[0] > highestGrouping:
        highestGrouping = value[0]
        highestCard = value
    
    
print(values)


