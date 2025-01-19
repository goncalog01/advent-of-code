with open("input.txt", "r") as f:
    lines = [line for line in f.read().splitlines() if line != ""]

fields = ()

i = 0

while lines[i] != "your ticket:":
    fields += ((int(lines[i].split(": ")[1].split(" or ")[0].split("-")[0]), int(lines[i].split(": ")[1].split(" or ")[0].split("-")[1]), int(lines[i].split(": ")[1].split(" or ")[1].split("-")[0]), int(lines[i].split(": ")[1].split(" or ")[1].split("-")[1])),)
    i += 1

sum = 0

for line in lines[i + 3:]:
    ticket = [int(x) for x in line.split(",")]
    for n in ticket:
        valid = False
        for field in fields:
            if field[0] <= n <= field[1] or field[2] <= n <= field[3]:
                valid = True
                break
        if not valid:
            sum += n

print(sum)