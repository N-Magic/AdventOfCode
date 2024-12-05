import sys
from collections import defaultdict, deque

# Read input
file = open(sys.argv[1]).read().strip()

orderRules = []
updatePages = []

answer = 0
orderingRules = True

# Topological sorting logic (reuse from earlier)
def topological_sort(nodes, adjacency, in_degree):
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_list = []

    while queue:
        node = queue.popleft()
        sorted_list.append(node)

        for neighbor in adjacency[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_list) != len(nodes):
        raise ValueError("Cycle detected! The rules are inconsistent.")

    return sorted_list

# Check if pages are sorted according to the rules
def checkIfSorted(pages):
    setIsGood = True
    for i in range(len(pages) - 1):
        twoPagesGood = False
        for orderRule in orderRules:
            if (pages[i] == orderRule[0]) and (pages[i+1] == orderRule[1]):
                twoPagesGood = True
        if not twoPagesGood:
            setIsGood = False
    return setIsGood

# Parse input data
for line in file.splitlines():
    if orderingRules:
        if (line == ""):
            orderingRules = False
            continue
        else:
            orderRules.append([line.split("|")[0], line.split("|")[1]])
    else:
        updatePages.append(line.split(","))

# Prepare for topological sorting
adjacency = defaultdict(list)
in_degree = defaultdict(int)
all_elements = set()

for u, v in orderRules:
    adjacency[u].append(v)
    in_degree[v] += 1
    if u not in in_degree:
        in_degree[u] = 0
    all_elements.add(u)
    all_elements.add(v)

missOrdered = []

# Step 1: Sort all elements based on the rules (topological sort)
sorted_pages = topological_sort(all_elements, adjacency, in_degree)

# Step 2: Create a mapping from page to its position in the sorted order
page_position = {page: idx for idx, page in enumerate(sorted_pages)}

# Process the pages
for pages in updatePages:
    # Sort pages based on the precomputed sorted order
    sorted_pages_for_this_list = sorted(pages, key=lambda x: page_position[x])

    # Check if the list was sorted correctly
    if pages == sorted_pages_for_this_list:
        # If the list is already sorted, add the middle element to the answer
        answer += int(pages[len(pages) // 2])
    else:
        # Otherwise, add the misordered list to missOrdered
        missOrdered.append(pages)

secondAnswer = 0
print(len(missOrdered))

# Step 3: Optionally print sorted lists
for wrong in missOrdered:
    print("TryingToSort")
    print(sorted(wrong, key=lambda x: page_position[x]))

print(secondAnswer)
