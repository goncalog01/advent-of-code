with open("input.txt", "r") as f:
    heightmap = f.read().splitlines()

num_lines = len(heightmap)
num_cols = len(heightmap[0])

sum = 0

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
            sum += int(heightmap[i][j]) + 1

print(sum)