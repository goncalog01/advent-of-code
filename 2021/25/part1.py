with open("input.txt", "r") as f:
    map = f.read().splitlines()

x_r = len(map[0])
y_r = len(map)

east = set([(i,j) for j in range(y_r) for i in range(x_r) if map[j][i] == ">"])
south = set([(i,j) for j in range(y_r) for i in range(x_r) if map[j][i] == "v"])

steps = 0

while True:
    moved = False
    new_east = set()
    new_south = set()
    for cucumber in east:
        new_cucumber = ((cucumber[0] + 1) % x_r, cucumber[1])
        if new_cucumber not in east and new_cucumber not in south:
            new_east.add(new_cucumber)
            moved = True
        else:
            new_east.add(cucumber)
    for cucumber in south:
        new_cucumber = (cucumber[0], (cucumber[1] + 1) % y_r)
        if new_cucumber not in new_east and new_cucumber not in south:
            new_south.add(new_cucumber)
            moved = True
        else:
            new_south.add(cucumber)
    steps += 1
    if not moved:
        break
    east = new_east
    south = new_south

print(steps)