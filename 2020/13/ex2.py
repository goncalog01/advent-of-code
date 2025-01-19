with open("input.txt", "r") as f:
    lines = f.read().splitlines()

bus_ids = [(int(b), i) for i, b in enumerate(lines[1].split(",")) if b != "x"]

jump = i = bus_ids[0][0] 
for b in bus_ids[1:]:
    while (i + b[1]) % b[0] != 0:
        i += jump
    jump *= b[0]

print(i)