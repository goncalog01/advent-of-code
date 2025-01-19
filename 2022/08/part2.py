def score_left(trees, x, y):
    viewing_distance = 0
    for i in range(x - 1, -1, -1):
        viewing_distance += 1
        if int(trees[y][i]) >= int(trees[y][x]):
            break
    return viewing_distance

def score_right(trees, x, y):
    viewing_distance = 0
    for i in range(x + 1, len(trees[0])):
        viewing_distance += 1
        if int(trees[y][i]) >= int(trees[y][x]):
            break
    return viewing_distance

def score_top(trees, x, y):
    viewing_distance = 0
    for i in range(y - 1, -1, -1):
        viewing_distance += 1
        if int(trees[i][x]) >= int(trees[y][x]):
            break
    return viewing_distance

def score_bottom(trees, x, y):
    viewing_distance = 0
    for i in range(y + 1, len(trees)):
        viewing_distance += 1
        if int(trees[i][x]) >= int(trees[y][x]):
            break
    return viewing_distance

with open("input.txt", "r") as f:
    trees = f.read().splitlines()

max_score = 0

for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[0]) - 1):
        scenic_score = score_left(trees, x, y) * score_right(trees, x, y) * score_top(trees, x, y) * score_bottom(trees, x, y)
        if scenic_score > max_score:
            max_score = scenic_score

print(max_score)