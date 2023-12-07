import sys
total = 0
data = open(sys.argv[1]).read().splitlines()
print(data[0])
races = data[0].split()
distances =  data[1].split()
races.pop(0)
distances.pop(0)

i = 0
j = 0
while i < int(races[0]):
    distance = (i * 1) * (int(races[0])-i)
    print(distance)
    i += 1
    if distance > int(distances[0]):
        j += 1

i = 0
k = 0
while i < int(races[1]):
    distance = (i * 1) * (int(races[1])-i)
    print(distance)
    i += 1
    if distance > int(distances[1]):
        k += 1

i = 0
l = 0
while i < int(races[2]):
    distance = (i * 1) * (int(races[2])-i)
    print(distance)
    i += 1
    if distance > int(distances[2]):
        l += 1

i = 0
m = 0
while i < int(races[3]):
    distance = (i * 1) * (int(races[3])-i)
    print(distance)
    i += 1
    if distance > int(distances[3]):
        m += 1
print("wins  " + str(j*k*l*m))
