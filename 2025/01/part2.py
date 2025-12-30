with open("input.txt", "r") as f:
    lines = f.read().splitlines()

point = 50
total = 0

for line in lines:
    rotate = int(line[1:])
    remain = rotate % 100
    total += rotate // 100

    if line[0] == "L":
        if point != 0 and point - remain <= 0:
            total += 1
        point = (point - remain) % 100
    else:
        if point != 0 and point + remain >= 100:
            total += 1
        point = (point + remain) % 100

print(total)