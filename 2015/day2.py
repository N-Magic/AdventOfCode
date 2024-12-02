import sys
file = open(sys.argv[1]).read().strip()

totalArea = 0

def surfaceArea(l,w,h):
    sides = [l,w,h]
    sides.sort()
    smallest =sides[0]*sides[1]
    minimumArea = (2 * ((l*w) + (w*h) + (h*l)))
    return smallest + minimumArea

for line in file.split("\n"):
    dimensions = line.split("x")
    area = surfaceArea(int(dimensions[0]),int(dimensions[1]),int(dimensions[2]))
    totalArea += area
print(totalArea)
