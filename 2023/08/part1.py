with open("input.txt", "r") as f:
    lines = f.read().splitlines()

directions = lines[0]
map = {}

for line in lines[2:]:
    node, dirs = line.split(" = ")
    left, right = dirs[1:-1].split(", ")
    map[node] = { "L" : left, "R" : right }

current = "AAA"
steps = 0

while current != "ZZZ":
    current = map[current][directions[steps % len(directions)]]
    steps += 1

print(steps)