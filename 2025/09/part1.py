with open("input.txt", "r") as f:
    tiles = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

def area(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)

largest_area = 0
for i in range(len(tiles)):
    for tile in tiles[i+1:]:
        largest_area = max(largest_area, area(tiles[i], tile))

print(largest_area)