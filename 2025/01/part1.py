with open("input.txt", "r") as f:
    lines = f.read().splitlines()

point = 50
total = 0

for line in lines:
    if line[0] == "L":
        point = (point - int(line[1:])) % 100
    else:
        point = (point + int(line[1:])) % 100

    if point == 0:
        total += 1

print(total)