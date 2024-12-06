import re
import sys

file = open(sys.argv[1]).read().strip()

expressionOne = r"(\w\w)\w*\1"
expressionTwo = r"(\w).(\1)"

total = 0

for line in file.splitlines():
    if re.search(expressionOne, line) and re.search(expressionTwo, line):
        total += 1
        print(line)
print(total)
