def visible_left(trees, x, y):
    for i in range(x - 1, -1, -1):
        if int(trees[y][i]) >= int(trees[y][x]):
            return False
    return True

def visible_right(trees, x, y):
    for i in range(x + 1, len(trees[0])):
        if int(trees[y][i]) >= int(trees[y][x]):
            return False
    return True

def visible_top(trees, x, y):
    for i in range(0, y):
        if int(trees[i][x]) >= int(trees[y][x]):
            return False
    return True

def visible_bottom(trees, x, y):
    for i in range(y + 1, len(trees)):
        if int(trees[i][x]) >= int(trees[y][x]):
            return False
    return True

with open("input.txt", "r") as f:
    trees = f.read().splitlines()

visible_trees = 2 * len(trees) + 2 * len(trees[0]) - 4

for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[0]) - 1):
        if visible_left(trees, x, y) or visible_right(trees, x, y) or visible_top(trees, x, y) or visible_bottom(trees, x, y):
            visible_trees += 1

print(visible_trees)