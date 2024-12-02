from sys import argv
from math import inf

data = open(argv[1] or input("file: ")).read().splitlines()

seeds = list(map(int, data[0].split("seeds: ")[1].split()))

result_seed = inf

translates = []
tracking = []

for line in data:
    if len(line) == 0 or line.endswith(":"):
        if tracking != []:
            translates.append(tracking)
            tracking = []
    elif line[0].isdigit():
        dest, src, length = line.split()
        tracking.append([int(dest), int(src), int(length)])

for i in range(0, int(len(seeds) / 2), 2):
    for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
        for translation in translates:
            for dest, src, length in translation:
                if seed in range(src, src + length):
                    seed += dest - src
                    break

        result_seed = min(result_seed, seed)

print("result:", result_seed)