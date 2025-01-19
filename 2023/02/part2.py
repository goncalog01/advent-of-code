with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    game = line.split(": ")[1]
    sets = game.split("; ")
    colors = {"red" : 0, "green" : 0, "blue" : 0}
    for s in sets:
        cubes = s.split(", ")
        for cube in cubes:
            num, color = cube.split(" ")
            if colors[color] < int(num):
                colors[color] = int(num)
    power = 1
    for color in colors:
        power *= colors[color]
    total += power

print(total)