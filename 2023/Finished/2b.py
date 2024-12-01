import sys

data = open(sys.argv[1]).read().splitlines()

total = 0 

for line in data:
    game_number = line.split(":")[0].split(" ")[-1]


for line in data:
    maxGreen = 1
    maxRed = 1
    maxBlue = 1

    game_number = line.split(":")[0].split(" ")[-1]

    game_parts = line.split(":")[1].split(";")

    for part in game_parts:
        cube_data = part.split(" ")
        cube_data.pop(0)
        # print(cube_data)
        i = 0
        for piece in cube_data:
            if piece.isdigit():
                i = int(piece)
            else:
                if piece.replace(",","") == 'green':
                    if i >= maxGreen:
                        maxGreen = i
                if piece.replace(",","") == 'red':
                    if i >= maxRed:
                        maxRed = i
                if piece.replace(",","") == 'blue':
                    if i >= maxBlue:
                        maxBlue = i
    roundpow = maxRed * maxGreen * maxBlue
    total = roundpow + total
print(total)


                
