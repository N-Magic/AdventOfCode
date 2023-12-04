import sys
D = open(sys.argv[1]).read().strip()
total = 0
digits = []
for line in D.splitlines():
    digits = []
    for i, c in enumerate(line): 
        if c.isdigit():
            digits.append(int(c))
        for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    total = total + int(str(digits[0]) + str(digits[-1]))
print("Hi")
print(total)
print("END")

