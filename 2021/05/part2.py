def points_between(x1, y1, x2, y2):
    while True:
        yield (x1, y1)

        if x1 == x2 and y1 == y2:
            return
        if x1 != x2:
            x1 += (1 if x1 < x2 else -1)
        if y1 != y2:
            y1 += (1 if y1 < y2 else -1)

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

points = {}

for line in lines:
    p1, p2 = line.split(" -> ")

    x1, y1 = p1.split(",")
    x2, y2 = p2.split(",")

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    for (x, y) in points_between(x1, y1, x2, y2):
        if (x, y) in points:
            points[(x, y)] += 1
        else:
            points[(x, y)] = 1

overlaps = 0

for point in points:
    if points[point] >= 2:
        overlaps += 1

print(overlaps)