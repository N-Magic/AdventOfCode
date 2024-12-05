import sys
import hashlib

input = open(sys.argv[1]).read().strip()

def hash(string):
    return hashlib.md5(string.encode()).hexdigest()

i = 0
while True:
    item = hash(str(input + str(i)))
    if(item[:5] == "00000"):
        print(i)
        break
    i += 1

i = 0
while True:
    item = hash(str(input + str(i)))
    if(item[:6] == "000000"):
        print(i)
        break
    i += 1
