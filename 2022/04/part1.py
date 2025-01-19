with open("input.txt", "r") as f:
    pairs = f.read().splitlines()

contains = 0

for pair in pairs:
    a, b = pair.split(",")
    a1, a2 = [int(x) for x in a.split("-")]
    b1, b2 = [int(x) for x in b.split("-")]
    if (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a2 <= b2):
        contains += 1

print(contains)