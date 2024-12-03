import sys
import hashlib

input = open(sys.argv[1]).read().strip()

def hash(string):
    return hashlib.md5(string.encode())

print(hash(input))
