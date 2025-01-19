import math

with open("input.txt", "r") as f:
    instructions = f.read().splitlines()

points = []
i = 0
for i in range(len(instructions)):
    if instructions[i] == "":
        break
    x, y = instructions[i].split(",")
    points += [ { "x" : int(x), "y" : int(y) } ]

folds = []
for fold in instructions[i+1:]:
    folds += [(fold.split("fold along ")[1].split("=")[0], int(fold.split("fold along ")[1].split("=")[1]))]

for fold in folds:
    i = 0
    while i < len(points):
        if points[i][fold[0]] > fold[1]:
            new_point = points[i]
            new_point[fold[0]] = new_point[fold[0]] - ((new_point[fold[0]] - fold[1]) * 2)
            points.remove(points[i])
            if new_point not in points:
                points += [new_point]
        else:
            i += 1

min_x = math.inf
min_y = math.inf
max_x = -math.inf
max_y = -math.inf

for point in points:
    if point["x"] < min_x:
        min_x = point["x"]
    if point["y"] < min_y:
        min_y = point["y"]
    if point["x"] > max_x:
        max_x = point["x"]
    if point["y"] > max_y:
        max_y = point["y"]

for point in points:
    if min_x < 0:
        point["x"] += abs(min_x)
    if min_y < 0:
        point["y"] += abs(min_y)

for i in range(max_y + 1):
    line = ""
    for j in range(max_x + 1):
        if { "x" : j, "y" : i } in points:
            line += "#"
        else:
            line += "."
    print(line)