import re
import sys

file = open(sys.argv[1]).read().strip()

expressionOne = r"(\w*[aeiou]\w*){3,}"
expressionTwo = r"(\w)\1"
expressionThree = r"ab|cd|pq|xy"

total = 0

for line in file.splitlines():
    if re.search(expressionOne, line) and re.search(expressionTwo, line):
        if not re.search(expressionThree, line):
            total += 1
            print(line)
print(total)
