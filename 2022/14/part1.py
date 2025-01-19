def points_between(p1, p2):
    points = []
    if p1[0] == p2[0]:
        if p1[1] < p2[1]:
            for y in range(p1[1], p2[1] + 1):
                points.append((p1[0], y))
        else:
            for y in range(p2[1], p1[1] + 1):
                points.append((p1[0], y))
    elif p1[1] == p2[1]:
        if p1[0] < p2[0]:
            for x in range(p1[0], p2[0] + 1):
                points.append((x, p1[1]))
        else:
            for x in range(p2[0], p1[0] + 1):
                points.append((x, p1[1]))
    return points

def produce_unit(blocked_tiles, max_y):
    unit = (500, 0)
    while True:
        if unit[1] == max_y:
            return (False, unit)
        elif (unit[0], unit[1] + 1) not in blocked_tiles:
            unit = (unit[0], unit[1] + 1)
        elif (unit[0] - 1, unit[1] + 1) not in blocked_tiles:
            unit = (unit[0] - 1, unit[1] + 1)
        elif (unit[0] + 1, unit[1] + 1) not in blocked_tiles:
            unit = (unit[0] + 1, unit[1] + 1)
        else:
            return (True, unit)

with open("input.txt", "r") as f:
    rocks = f.read().splitlines()

blocked_tiles = []
max_y = 0
for rock in rocks:
    points = rock.split(" -> ")
    for i in range(0, len(points) - 1):
        p1 = [int(x) for x in points[i].split(",")]
        p2 = [int(x) for x in points[i+1].split(",")]
        blocked_tiles.extend(points_between(p1, p2))
        if max(p1[1], p2[1]) > max_y:
            max_y = max(p1[1], p2[1])
blocked_tiles = list(dict.fromkeys(blocked_tiles))

units_sand = 0
while True:
    res = produce_unit(blocked_tiles, max_y)
    if res[0]:
        blocked_tiles.append(res[1])
        units_sand += 1
    else:
        break
print(units_sand)