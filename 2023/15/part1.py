with open("input.txt", "r") as f:
    steps = f.read().split(",")

total = 0
for step in steps:
    current = 0
    for char in step:
        current += ord(char)
        current *= 17
        current %= 256
    total += current

print(total)