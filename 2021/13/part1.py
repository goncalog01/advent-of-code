with open("input.txt", "r") as f:
    instructions = f.read().splitlines()

points = []
i = 0
for i in range(len(instructions)):
    if instructions[i] == "":
        break
    x, y = instructions[i].split(",")
    points += [ { "x" : int(x), "y" : int(y) } ]

fold = (instructions[i+1].split("fold along ")[1].split("=")[0], int(instructions[i+1].split("fold along ")[1].split("=")[1]))

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

print(len(points))