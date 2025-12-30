with open("input.txt", "r") as f:
    grid = f.read().splitlines()

def adjacent_positions(grid, i, j):
    max_x = len(grid[0])
    max_y = len(grid)
    adjacent = [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i - 1, j), (i + 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]
    valid = []

    for (x, y) in adjacent:
        if 0 <= x < max_x and 0 <= y < max_y:
            valid.append((x, y))

    return valid

rolls = []
empty = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "@":
            rolls.append((x, y))
        else:
            empty.append((x, y))

total = 0

while True:
    removed = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in empty:
                continue
            adjacent = 0
            for (i, j) in adjacent_positions(grid, x, y):
                if (i, j) in rolls:
                    adjacent += 1
            if adjacent < 4:
                rolls.remove((x, y))
                empty.append((x, y))
                removed += 1
                total += 1

    if removed == 0:
        break

print(total)