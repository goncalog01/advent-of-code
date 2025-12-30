with open("input.txt", "r") as f:
    input = f.read().split("\n\n")

presents_size = []
for line in input[:-1]:
    presents_size.append(line.count("#"))

regions = []
for line in input[-1].split("\n"):
    l, r = line.split(": ")
    x, y = map(int, l.split("x"))
    regions.append({"dimensions" : (x, y), "presents" : list(map(int, r.split(" ")))})

total = 0
for region in regions:
    x, y = region["dimensions"]
    present_space = 0
    for i, n in enumerate(region["presents"]):
        present_space += n * presents_size[i]
    if present_space <= (x * y):
        total += 1

print(total)