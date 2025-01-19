import math

def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))

def slice_to_str(cubes, range_x, range_y, z):
    slice = []
    for y in range(range_y[0], range_y[1] + 1):
        s = ""
        for x in range(range_x[0], range_x[1] + 1):
            if [x, y, z] in cubes:
                s += "#"
            else:
                s += "."
        slice.append(s)
    return slice

def get_air_cubes(cubes, range_x, range_y, z):
    slice = slice_to_str(cubes, range_x, range_y, z)
    air_cubes = []
    for y in range(len(slice)):
        l = slice[y].find("#")
        r = slice[y].rfind("#")
        for x in range(l + 1, r):
            if slice[y][x] == ".":
                air_cubes.append([range_x[0] + x, range_y[0] + y, z])
    return air_cubes

with open("input.txt", "r") as f:
    data = f.read().splitlines()

cubes = [[int(x) for x in data[i].split(",")] for i in range(len(data))]
range_x = [math.inf, -math.inf]
range_y = [math.inf, -math.inf]
range_z = [math.inf, -math.inf]
for cube in cubes:
    range_x[0] = min(range_x[0], cube[0])
    range_x[1] = max(range_x[1], cube[0])
    range_y[0] = min(range_y[0], cube[1])
    range_y[1] = max(range_y[1], cube[1])
    range_z[0] = min(range_z[0], cube[2])
    range_z[1] = max(range_z[1], cube[2])
    
for s in slice_to_str(cubes, range_x, range_y, 1):
    print(s)

for z in range(range_z[0], range_z[1] + 1):
    cubes.extend(get_air_cubes(cubes, range_x, range_y, z))

for s in slice_to_str(cubes, range_x, range_y, 1):
    print(s)

exposed = [6 for _ in cubes]
for i in range(len(cubes)):
    for j in range(i + 1, len(cubes)):
        if manhattan(cubes[i], cubes[j]) == 1:
            exposed[i] -= 1
            exposed[j] -= 1
#print(sum(exposed))