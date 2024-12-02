import sys
file = open(sys.argv[1]).read().strip()

totalLength = 0

def ribbon(l,w,h):
    volume = l * w * h
    sides = [l,w,h]
    sides.sort()
    length = 2 * (sides[0] + sides[1])
    return volume + length

for line in file.split("\n"):
    dimensions = line.split("x")
    length = ribbon(int(dimensions[0]),int(dimensions[1]),int(dimensions[2]))
    totalLength += length
print(totalLength)
