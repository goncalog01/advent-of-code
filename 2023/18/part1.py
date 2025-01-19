with open("input.txt", "r") as f:
    lines = f.read().splitlines()

curr = (0, 0)
points = [curr]
x_range = [0, 0]
y_range = [0, 0]
for line in lines:
    dir, num, color = line.split(" ")
    match dir:
        case "U":
            dx = 0
            dy = -1
        case "D":
            dx = 0
            dy = 1
        case "L":
            dx = -1
            dy = 0
        case "R":
            dx = 1
            dy = 0


    for _ in range(int(num)):
        curr = (curr[0] + dx, curr[1] + dy)
        points.append(curr)
        if curr[0] < x_range[0]:
            x_range[0] = curr[0]
        if curr[0] > x_range[1]:
            x_range[1] = curr[0]
        if curr[1] < y_range[0]:
            y_range[0] = curr[1]
        if curr[1] > y_range[1]:
            y_range[1] = curr[1]

map = []
for y in range(y_range[0] - 1, y_range[1] + 2):
    s = ""
    for x in range(x_range[0] - 1, x_range[1] + 2):
        if (x, y) in points:
            s += "#"
        else:
            s += "."
    map.append(s)

visited = []
to_visit = [(0, 0)]
while len(to_visit) > 0:
    x, y = to_visit.pop()
    if 0 <= x - 1 < len(map[0]) and 0 <= y < len(map) and map[y][x - 1] != "#" and (x - 1, y) not in to_visit and (x - 1, y) not in visited:
        to_visit.append((x - 1, y))
    if 0 <= x + 1 < len(map[0]) and 0 <= y < len(map) and map[y][x + 1] != "#" and (x + 1, y) not in to_visit and (x + 1, y) not in visited:
        to_visit.append((x + 1, y))
    if 0 <= x < len(map[0]) and 0 <= y - 1 < len(map) and map[y - 1][x] != "#" and (x, y - 1) not in to_visit and (x, y - 1) not in visited:
        to_visit.append((x, y - 1))
    if 0 <= x  < len(map[0]) and 0 <= y + 1 < len(map) and map[y + 1][x] != "#" and (x, y + 1) not in to_visit and (x, y + 1) not in visited:
        to_visit.append((x, y + 1))
    visited.append((x, y))

print(len(map) * len(map[0]) - len(visited))