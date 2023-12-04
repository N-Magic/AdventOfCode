import sys

data = open(sys.argv[1]).read().splitlines()

total = 0 

maxGreen = 13
maxRed = 12
maxBlue = 14

valid = True

for line in data:
    game_number = line.split(":")[0].split(" ")[-1]


for line in data:
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
                    if i <= maxGreen:
                        print("Working")
                    else:
                        valid = False
                if piece.replace(",","") == 'red':
                    if i <= maxRed:
                        print("Working")
                    else:
                        valid = False
                if piece.replace(",","") == 'blue':
                    if i <= maxBlue:
                        print("Working")
                    else:
                        valid = False
    if valid:
        total = int(game_number) + total
        print(total)
    else:
        print("invalid")
        valid = True
print(total)


                
