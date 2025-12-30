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

accessible = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == ".":
            continue
        rolls = 0
        for (i, j) in adjacent_positions(grid, x, y):
            if grid[j][i] == "@":
                rolls += 1
        if rolls < 4:
            accessible += 1

print(accessible)