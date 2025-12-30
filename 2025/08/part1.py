import math

with open("input.txt", "r") as f:
    boxes = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

distances = dict()
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distances[(i, j)] = math.dist(boxes[i], boxes[j])

sorted_distances = sorted(distances.keys(), key=lambda x: distances[x])
sets = []
for (b1, b2) in sorted_distances[:1000]:
    set_b1 = None
    set_b2 = None
    for s in sets:
        if b1 in s:
            set_b1 = s
        if b2 in s:
            set_b2 = s

    if set_b1 and set_b2:
        if set_b1 is not set_b2:
            set_b1 |= set_b2
            sets.remove(set_b2)
    elif set_b1:
        set_b1.add(b2)
    elif set_b2:
        set_b2.add(b1)
    else:
        sets.append({b1, b2})

total = 1
for s in sorted(sets, key=lambda x: len(x))[-3:]:
    total *= len(s)
print(total)