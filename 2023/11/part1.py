def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

empty_rows = [i for i, line in enumerate(lines) if "#" not in line]
empty_columns = [i for i in range(len(lines[0])) if all(line[i] != "#" for line in lines)]
galaxies = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append((x, y))

total = 0
for i, g in enumerate(galaxies):
    for galaxy in galaxies[i+1:]:
        rows_between = [row for row in empty_rows if min(g[1], galaxy[1]) < row < max(g[1], galaxy[1])]
        columns_between = [col for col in empty_columns if min(g[0], galaxy[0]) < col < max(g[0], galaxy[0])]
        total += manhattan_distance(g, galaxy) + len(rows_between) + len(columns_between)
    
print(total)