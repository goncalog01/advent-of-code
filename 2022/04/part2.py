with open("input.txt", "r") as f:
    pairs = f.read().splitlines()

overlaps = 0

for pair in pairs:
    a, b = pair.split(",")
    a1, a2 = [int(x) for x in a.split("-")]
    b1, b2 = [int(x) for x in b.split("-")]
    if a2 >= b1 and a1 <= b2:
        overlaps += 1

print(overlaps)