def hash(label):
    current = 0
    for char in label:
        current += ord(char)
        current *= 17
        current %= 256
    return current

with open("input.txt", "r") as f:
    steps = f.read().split(",")

boxes = [[] for i in range(256)]

for step in steps:
    if "-" in step:
        op = "-"
        op_i = step.index("-")
        label = step[:op_i]
    elif "=" in step:
        op = "="
        op_i = step.index("=")
        label = step[:op_i]
        focal_length = int(step[op_i + 1:])

    box = hash(label)

    if op == "-":
        for i, lens in enumerate(boxes[box]):
            if lens[0] == label:
                boxes[box].pop(i)
                break
    elif op == "=":
        for i, lens in enumerate(boxes[box]):
            if lens[0] == label:
                boxes[box][i][1] = focal_length
                break
        else:
            boxes[box].append([label, focal_length])

total = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        total += (i + 1) * (j + 1) * lens[1]

print(total)