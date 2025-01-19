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

for i, rock in enumerate(round_rocks):
    x = rock[0]
    y = rock[1]
    while y != 0:
        if (x, y - 1) in round_rocks or (x, y - 1) in cube_rocks:
            break
        y -= 1
    round_rocks[i] = (x, y)

total = 0
for rock in round_rocks:
    total += len(lines) - rock[1]

print(total)