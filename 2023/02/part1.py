with open("input.txt", "r") as f:
    lines = f.read().splitlines()

l = len(lines)
total = 0
for i in range(l):
    possible = True
    game = lines[i].split(": ")[1]
    sets = game.split("; ")
    for s in sets:
        colors = {"red" : 0, "green" : 0, "blue" : 0}
        cubes = s.split(", ")
        for cube in cubes:
            num, color = cube.split(" ")
            colors[color] = int(num)
        if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
            possible = False
            break
    if possible:
        total += i + 1

print(total)