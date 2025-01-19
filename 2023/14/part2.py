from copy import deepcopy

def print_map(round_rocks, cube_rocks, max_x, max_y):
    for y in range(max_y):
        s = ""
        for x in range(max_x):
            if (x, y) in round_rocks:
                s += "O"
            elif (x, y) in cube_rocks:
                s += "#"
            else:
                s += "."
        print(s)
        s = ""

def do_cycle(map, round_rocks, cube_rocks):
    dirs = ["north", "west", "south", "east"]
    for dir in dirs:
        round_rocks = tilt_platform(map, round_rocks, cube_rocks, dir)
    return round_rocks

def tilt_platform(map, round_rocks, cube_rocks, dir):
    if dir == "north":
        for i in range(len(map)):
            for j, rock in enumerate(round_rocks):
                x = rock[0]
                y = rock[1]
                if y == i:
                    while y != 0:
                        if (x, y - 1) in round_rocks or (x, y - 1) in cube_rocks:
                            break
                        y -= 1
                    round_rocks[j] = (x, y)
    elif dir == "west":
        for i in range(len(map[0])):
            for j, rock in enumerate(round_rocks):
                x = rock[0]
                y = rock[1]
                if x == i:
                    while x != 0:
                        if (x - 1, y) in round_rocks or (x - 1, y) in cube_rocks:
                            break
                        x -= 1
                    round_rocks[j] = (x, y)
    elif dir == "south":
        for i in range(len(map) - 1, -1, -1):
            for j, rock in enumerate(round_rocks):
                x = rock[0]
                y = rock[1]
                if y == i:
                    while y != len(map) - 1:
                        if (x, y + 1) in round_rocks or (x, y + 1) in cube_rocks:
                            break
                        y += 1
                    round_rocks[j] = (x, y)
    elif dir == "east":
        for i in range(len(map[0]) - 1, -1, -1):
            for j, rock in enumerate(round_rocks):
                x = rock[0]
                y = rock[1]
                if x == i:
                    while x != len(map[0]) - 1:
                        if (x + 1, y) in round_rocks or (x + 1, y) in cube_rocks:
                            break
                        x += 1
                    round_rocks[j] = (x, y)
    return round_rocks

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

round_rocks = []
cube_rocks = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "O":
            round_rocks.append((x, y))
        elif char == "#":
            cube_rocks.append((x, y))

cycles = [set(round_rocks)]
while True:
    round_rocks = do_cycle(lines, round_rocks, cube_rocks)
    round_rocks_cycle = set(round_rocks)
    if round_rocks_cycle in cycles:
        period_start = cycles.index(round_rocks_cycle)
        break
    cycles.append(round_rocks_cycle)

period_len = len(cycles) - period_start

total = 0
for rock in cycles[(1000000000 - period_start) % period_len + period_start]:
    total += len(lines) - rock[1]

print(total)