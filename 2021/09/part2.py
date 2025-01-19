with open("input.txt", "r") as f:
    heightmap = f.read().splitlines()

num_lines = len(heightmap)
num_cols = len(heightmap[0])

low_points = []

for i in range(num_lines):
    for j in range(num_cols):
        adj = []
        if i > 0:
            adj += [heightmap[i-1][j]]
        if j > 0:
            adj += [heightmap[i][j-1]]
        if i < num_lines - 1:
            adj += [heightmap[i+1][j]]
        if j < num_cols - 1:
            adj += [heightmap[i][j+1]]
        
        low_point = True

        for pos in adj:
            if int(pos) <= int(heightmap[i][j]):
                low_point = False
                break
        if low_point:
            low_points += [(i, j)]

sizes = [0, 0, 0]

for low_point in low_points:
    points = [low_point]

    k = 0

    while k < len(points):
        i = points[k][0]
        j = points[k][1]

        if i > 0 and int(heightmap[i-1][j]) >= int(heightmap[i][j]) and int(heightmap[i-1][j]) != 9 and (i-1, j) not in points:
            points += [(i-1, j)]
        if j > 0 and int(heightmap[i][j-1]) >= int(heightmap[i][j]) and int(heightmap[i][j-1]) != 9 and (i, j-1) not in points:
            points += [(i, j-1)]
        if i < num_lines - 1 and int(heightmap[i+1][j]) >= int(heightmap[i][j]) and int(heightmap[i+1][j]) != 9 and (i+1, j) not in points:
            points += [(i+1, j)]
        if j < num_cols - 1 and int(heightmap[i][j+1]) >= int(heightmap[i][j]) and int(heightmap[i][j+1]) != 9 and (i, j+1) not in points:
            points += [(i, j+1)]

        k += 1

    size = len(points)
    sizes.sort()

    if size > sizes[0]:
        sizes[0] = size

print(sizes[0] * sizes[1] * sizes[2])