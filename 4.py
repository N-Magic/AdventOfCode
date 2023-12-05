import sys
total = 0
data = open(sys.argv[1]).read().splitlines()

for line in data:
    winning_numbers = line.split(":")[1].split("|")[0].split(" ")
    winning_numbers.pop(0)
    winning_numbers.pop(-1)
    while ("" in winning_numbers):
        winning_numbers.remove("")
    elf_numbers = line.split(":")[1].split("|")[0].split(" ")
    elf_numbers.pop(0)
    elf_numbers.pop(-1)
    while ("" in elf_numbers):
        elf_numbers.remove("")
    proc = 0
    for e in elf_numbers:
        for w in winning_numbers:
            if e == w:
                print(w,e)
                proc = 1 + proc
    total = proc + total
    print(proc)
print(total)