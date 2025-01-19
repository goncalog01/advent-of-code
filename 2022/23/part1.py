import math

def get_neighbors(elves, x, y):
    neighbors = dict()
    if (x - 1, y - 1) in elves.values():
        neighbors["NW"] = (x - 1, y - 1)
    if (x - 1, y) in elves.values():
        neighbors["W"] = (x - 1, y)
    if (x - 1, y + 1) in elves.values():
        neighbors["SW"] = (x - 1, y + 1)
    if (x, y - 1) in elves.values():
        neighbors["N"] = (x, y - 1)
    if (x, y + 1) in elves.values():
        neighbors["S"] = (x, y + 1)
    if (x + 1, y - 1) in elves.values():
        neighbors["NE"] = (x + 1, y - 1)
    if (x + 1, y) in elves.values():
        neighbors["E"] = (x + 1, y)
    if (x + 1, y + 1) in elves.values():
        neighbors["SE"] = (x + 1, y + 1)
    return neighbors

def empty_direction(neighbors, direction):
    match direction:
        case "N":
            if "N" not in neighbors and "NE" not in neighbors and "NW" not in neighbors:
                return True
            else:
                return False
        case "S":
            if "S" not in neighbors and "SE" not in neighbors and "SW" not in neighbors:
                return True
            else:
                return False
        case "W":
            if "W" not in neighbors and "NW" not in neighbors and "SW" not in neighbors:
                return True
            else:
                return False
        case "E":
            if "E" not in neighbors and "NE" not in neighbors and "SE" not in neighbors:
                return True
            else:
                return False

def move(x, y, direction):
    match direction:
        case "N":
            return (x, y - 1)
        case "S":
            return (x, y + 1)
        case "W":
            return (x - 1, y)
        case "E":
            return (x + 1, y)

with open("input.txt", "r") as f:
    data = f.read().splitlines()

elves_count = 0
elves = dict()
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            elves[elves_count] = (x, y)
            elves_count += 1

check = ["N", "S", "W", "E"]
for _ in range(10):
    propose = dict()
    for elf in elves:
        x, y = elves[elf]
        neighbors = get_neighbors(elves, x, y)
        if len(neighbors) == 0:
            propose[elf] = elves[elf]
        else:
            moved = False
            for direction in check:
                if empty_direction(neighbors, direction):
                    propose[elf] = move(x, y, direction)
                    moved = True
                    break
            if not moved:
                propose[elf] = elves[elf]
    for elf in elves:
        if list(propose.values()).count(propose[elf]) == 1:
            elves[elf] = propose[elf]
    check.append(check[0])
    check.remove(check[0])

x_range = [math.inf, -math.inf]
y_range = [math.inf, -math.inf]
for (x, y) in elves.values():
    x_range[0] = min(x_range[0], x)
    x_range[1] = max(x_range[1], x)
    y_range[0] = min(y_range[0], y)
    y_range[1] = max(y_range[1], y)
    
empty = 0
for y in range(y_range[0], y_range[1] + 1):
    for x in range(x_range[0], x_range[1] + 1):
        if (x, y) not in elves.values():
            empty += 1
print(empty)