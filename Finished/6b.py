import sys
total = 0
data = open(sys.argv[1]).read().splitlines()
print(data[0])
races = data[0].split()
distances =  data[1].split()
races.pop(0)
distances.pop(0)
racing = int(str(races[0]) + str(races[1]) + str(races[2]) + str(races[3]))
distancing = int(str(distances[0]) + str(distances[1]) + str(distances[2]) + str(distances[3]))

i = 0
j = 0
while i < int(racing):
    distance = (i * 1) * (int(racing)-i)
    # print(distance)
    i += 1
    if distance > int(distancing):
        j += 1

print("wins  " + str(j))
