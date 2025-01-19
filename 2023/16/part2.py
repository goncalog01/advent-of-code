import math

with open("input.txt", "r") as f:
    map = f.read().splitlines()

mirror = {
    "/" : {
        "right" : "up",
        "left" : "down",
        "up" : "right",
        "down" : "left"
    },
    "\\" : {
        "right" : "down",
        "left" : "up",
        "up" : "left",
        "down" : "right"
    }
}

starts = []
for i in range(len(map)):
    starts.append([(0, i), "right"])
    starts.append([(len(map[0]) - 1, i), "left"])
for i in range(len(map[0])):
    starts.append([(i, 0), "down"])
    starts.append([(i, len(map) - 1), "up"])

max_energized = -math.inf
for start in starts:
    passed = [start]
    energized = {start[0]}
    beams = [start]
    while len(beams) > 0:
        pos, dir = beams.pop()
        x = pos[0]
        y = pos[1]

        match dir:
            case "right":
                dx = 1
                dy = 0
            case "left":
                dx = -1
                dy = 0
            case "up":
                dx = 0
                dy = -1
            case "down":
                dx = 0
                dy = 1

        if map[y][x] == "/":
            dx, dy = -dy, -dx
            dir = mirror[map[y][x]][dir]
            if 0 <= x + dx < len(map[0]) and 0 <= y + dy < len(map) and [(x + dx, y + dy), dir] not in passed:
                beams.append([(x + dx, y + dy), dir])
                energized |= {(x + dx, y + dy)}
                passed.append([(x + dx, y + dy), dir])
        elif map[y][x] == "\\":
            dx, dy = dy, dx
            dir = mirror[map[y][x]][dir]
            if 0 <= x + dx < len(map[0]) and 0 <= y + dy < len(map) and [(x + dx, y + dy), dir] not in passed:
                beams.append([(x + dx, y + dy), dir])
                energized |= {(x + dx, y + dy)}
                passed.append([(x + dx, y + dy), dir])
        elif map[y][x] == "|" and (dir == "left" or dir == "right"):
            if 0 <= y - 1 < len(map) and [(x, y - 1), "up"] not in passed:
                beams.append([(x, y - 1), "up"])
                energized |= {(x, y - 1)}
                passed.append([(x, y - 1), "up"])
            if 0 <= y + 1 < len(map) and [(x, y + 1), "down"] not in passed:
                beams.append([(x, y + 1), "down"])
                energized |= {(x, y + 1)}
                passed.append([(x, y + 1), "down"])
        elif map[y][x] == "-" and (dir == "up" or dir == "down"):
            if 0 <= x - 1 < len(map[0]) and [(x - 1, y), "left"] not in passed:
                beams.append([(x - 1, y), "left"])
                energized |= {(x - 1, y)}
                passed.append([(x - 1, y), "left"])
            if 0 <= x + 1 < len(map[0]) and [(x + 1, y), "right"] not in passed:
                beams.append([(x + 1, y), "right"])
                energized |= {(x + 1, y)}
                passed.append([(x + 1, y), "right"])
        else:
            if 0 <= x + dx < len(map[0]) and 0 <= y + dy < len(map) and [(x + dx, y + dy), dir] not in passed:
                beams.append([(x + dx, y + dy), dir])
                energized |= {(x + dx, y + dy)}
                passed.append([(x + dx, y + dy), dir])
    
    if len(energized) > max_energized:
        max_energized = len(energized)

print(max_energized)