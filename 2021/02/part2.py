with open("input.txt", "r") as f:
    input = f.read().splitlines()

course = []

for line in input:
    course += [[line.split()[0], int(line.split()[1])]]

hor_pos = 0
depth = 0
aim = 0

for command in course:
    if command[0] == "forward":
        hor_pos += command[1]
        depth += aim * command[1]
    elif command[0] == "down":
        aim += command[1]
    elif command[0] == "up":
        aim -= command[1]

print(hor_pos * depth)