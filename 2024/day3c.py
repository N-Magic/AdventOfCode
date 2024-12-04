import re
import sys
total = 0
ahh = open(sys.argv[1]).read().strip()
inputString = ""
for line in ahh.splitlines():
    inputString += line + "$$$$"

beforeDontPattern = r'^(.*?)(?=don\'t\(\))'
inAllowedSpace = r'(?<=do\(\))(.*?)(?=don\'t\(\))'
mul_pattern = r'mul\((\d+),(\d+)\)'

allowed = re.findall(beforeDontPattern, inputString)
matches = re.findall(mul_pattern, allowed[0])
for match in matches:
    x = int(match[0])
    y = int(match[1])
    result = x * y
    total += result

allowed = re.findall(inAllowedSpace, inputString)
for part in allowed:
    matches = re.findall(mul_pattern, part)
    for match in matches:
        x = int(match[0])
        y = int(match[1])
        result = x * y
        total += result

print(total)
