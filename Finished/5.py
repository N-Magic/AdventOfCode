import sys
total = 0
data = open(sys.argv[1]).read().split(":")
seeds = data[1].splitlines()
seeds = seeds[0].split(" ")
while "" in seeds:
    seeds.remove("")
seedsINIT = seeds
i=0
first = 0
second = 0
p1 = 0
p2 = 0
loops = len(seedsINIT) + 2

seeds = []
while i < loops:
    print(i)
    if first == 0:
        first = int(seedsINIT[i])
    elif second == 0:
        second = int(seedsINIT[i])
    else:
        j = first
        while j < (first+second):
            # print(j)
            seeds.append(int(j))
            j = j + 1
        first = 0
        second = 0
    i = i + 1
    print(first,second)
    seeds = list(set(seeds))
while "" in seeds:
    seeds.remove("")
    
# Tuesday DEC 19th Party

# print(seeds)
# print(data)

seedTOsoil = data[2].splitlines()
while "" in seedTOsoil:
    seedTOsoil.remove("")
seedTOsoil.pop(-1)

soilTOfert = data[3].splitlines()
while "" in soilTOfert:
    soilTOfert.remove("")
soilTOfert.pop(-1)
# print(soilTOfert)

fertTOwater = data[4].splitlines()
while "" in fertTOwater:
    fertTOwater.remove("")
fertTOwater.pop(-1)

waterTOlight = data[5].splitlines()
while "" in waterTOlight:
    waterTOlight.remove("")
waterTOlight.pop(-1)
# print(waterTOlight)

lightTOtemp = data[6].splitlines()
while "" in lightTOtemp:
    lightTOtemp.remove("")
lightTOtemp.pop(-1)

tempTOhum = data[7].splitlines()
while "" in tempTOhum:
    tempTOhum.remove("")
tempTOhum.pop(-1)
# print(tempTOhum)

humTOloc = data[8].splitlines()
while "" in humTOloc:
    humTOloc.remove("")
humTOloc.pop(-1)

soils = []
ferts = []
waters = []
lights = []
temps = []
hums = []
locs = []

for i, seed in enumerate(seeds):
    seeds[i] = int(seed)
seeds = list(set(seeds))
print("seeds")
print(seeds)
for i, seed in enumerate(seeds):
    seeds[i] = int(seed)
print("seeds")
print(seeds)
for q, seed in enumerate(seeds):
    proc = False
    for soil in seedTOsoil:
        soil = soil.split(" ")
        # print(soil)
        if int(seed) >= int(soil[1]) and int(seed) <= (int(soil[1])+int(soil[2])):
            soils.append((int(seed) + int(soil[0]) - int(soil[1])))
            proc = True
            break
    if proc == False:
        soils.append(int(seed))
print("soils")
print(soils)
# print(soilTOfert)
for q, soil in enumerate(soils):
    proc = False
    for fert in soilTOfert:
        fert = fert.split(" ")
        if soil >= int(fert[1]) and soil <= (int(fert[1])+int(fert[2])):
            ferts.append((int(soil) + int(fert[0]) - int(fert[1])))
            proc = True
            break
    if proc == False:
        ferts.append(int(soil))
print("ferts")
print(ferts)

for q, fert in enumerate(ferts):
    proc = False
    for water in fertTOwater:
        water = water.split(" ")
        if fert >= int(water[1]) and fert <= (int(water[1])+int(water[2])):
            waters.append((int(fert) + int(water[0]) - int(water[1])))
            proc = True
            break
    if proc == False:
        waters.append(int(fert))
print("waters")
print(waters)
for q, water in enumerate(waters):
    proc = False
    for light in waterTOlight:
        light = light.split(" ")
        if water >= int(light[1]) and water <= (int(light[1])+int(light[2])):
            lights.append((int(water) + int(light[0]) - int(light[1])))
            proc = True
            break
    if proc == False:
        lights.append(int(water))
print("lights")
print(lights)
for q, light in enumerate(lights):
    proc = False
    for temp in lightTOtemp:
        temp = temp.split(" ")
        if light >= int(temp[1]) and light <= (int(temp[1])+int(temp[2])):
            temps.append((int(light) + int(temp[0]) - int(temp[1])))
            proc = True
            break
    if proc == False:
        temps.append(int(light))
print("temps")
print(temps)
for q, temp in enumerate(temps):
    proc = False
    for hum in tempTOhum:
        hum = hum.split(" ")
        if temp >= int(hum[1]) and temp <= (int(hum[1])+int(hum[2])):
            hums.append((int(temp) + int(hum[0]) - int(hum[1])))
            proc = True
            break
    if proc == False:
        hums.append(int(temp))
print("hums")
print(hums)
for q, hum in enumerate(hums):
    proc = False
    for loc in humTOloc:
        loc = loc.split(" ")
        if hum >= int(loc[1]) and hum <= (int(loc[1])+int(loc[2])):
            locs.append((int(hum) + int(loc[0]) - int(loc[1])))
            proc = True
            break
    if proc == False:
        locs.append(int(hum))
print("locs")
print(locs)
# print(locs)
total = locs[1]
for loc in locs:
    if int(loc) <= total:
        total = loc
print(total)