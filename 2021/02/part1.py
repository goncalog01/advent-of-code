with open("input.txt", "r") as f:
    input = f.read().splitlines()

course = []

for line in input:
    course += [[line.split()[0], int(line.split()[1])]]

hor_pos = 0
depth = 0

for command in course:
    if command[0] == "forward":
        hor_pos += command[1]
    elif command[0] == "down":
        depth += command[1]
    elif command[0] == "up":
        depth -= command[1]

print(hor_pos * depth)