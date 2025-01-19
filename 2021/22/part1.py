with open("input.txt", "r") as f:
    reboot_steps = f.read().splitlines()

cubes = []

for step in reboot_steps:
    op = step.split(" ")[0]
    _, a, b, c = step.split("=")
    dx = a[:-2].split("..")
    dx = [int(dx[0]), int(dx[1])]
    dy = b[:-2].split("..")
    dy = [int(dy[0]), int(dy[1])]
    dz = c.split("..")
    dz = [int(dz[0]), int(dz[1])]

    if dx[0] < -50 or dx[1] > 50 or dy[0] < -50 or dy[1] > 50 or dz[0] < -50 or dz[1] > 50:
        continue

    for i in range(len(cubes)):
        [x1, x2, y1, y2, z1, z2] = cubes[i]
        if dx[0] > x2 or dx[1] < x1 or dy[0] > y2 or dy[1] < y1 or dz[0] > z2 or dz[1] < z1:
            continue
        cubes[i] = None
        if dx[0] > x1:
            cubes.append((x1, dx[0] - 1, y1, y2, z1, z2))
        if dx[1] < x2:
            cubes.append((dx[1] + 1, x2, y1, y2, z1, z2))
        if dy[0] > y1:
            cubes.append((max(dx[0], x1), min(dx[1], x2), y1, dy[0] - 1, z1, z2))
        if dy[1] < y2:
            cubes.append((max(dx[0], x1), min(dx[1], x2), dy[1] + 1, y2, z1, z2))
        if dz[0] > z1:
            cubes.append((max(dx[0], x1), min(dx[1], x2), max(dy[0], y1), min(dy[1], y2), z1, dz[0] - 1))
        if dz[1] < z2:
            cubes.append((max(dx[0], x1), min(dx[1], x2), max(dy[0], y1), min(dy[1], y2), dz[1] + 1, z2))
    if op == "on":
        cubes.append((dx[0], dx[1], dy[0], dy[1], dz[0], dz[1]))
    cubes = [cube for cube in cubes if cube is not None]

count = 0
for cube in cubes:
    [x1, x2, y1, y2, z1, z2] = cube
    count += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

print(count)