from shapely.geometry import Polygon
from shapely.prepared import prep

with open("input.txt", "r") as f:
    tiles = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

def area(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)

shape = prep(Polygon(tiles))
largest_area = 0
for i in range(len(tiles)):
    x1, y1 = tiles[i]
    for (x2, y2) in tiles[i+1:]:
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        rectangle = Polygon([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])
        if shape.covers(rectangle):
            largest_area = max(largest_area, area(tiles[i], (x2, y2)))

print(largest_area)