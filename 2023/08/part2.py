from math import lcm

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

directions = lines[0]
map = {}
start = []

for line in lines[2:]:
    node, dirs = line.split(" = ")
    left, right = dirs[1:-1].split(", ")
    map[node] = { "L" : left, "R" : right }
    if node[-1] == "A":
        start.append(node)

steps_all = []

for node in start:
    current = node
    steps = 0
    while current[-1] != "Z":
        current = map[current][directions[steps % len(directions)]]
        steps += 1
    steps_all.append(steps)

print(lcm(*steps_all))