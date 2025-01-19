def are_touching(head, tail):
    return head["x"] - 1 <= tail["x"] <= head["x"] + 1 and head["y"] - 1 <= tail["y"] <= head["y"] + 1

def update_tail(head, tail):
    if head["x"] > tail["x"]:
        offset_x = 1
    elif head["x"] < tail["x"]:
        offset_x = -1
    else:
        offset_x = 0

    if head["y"] > tail["y"]:
        offset_y = 1
    elif head["y"] < tail["y"]:
        offset_y = -1
    else:
        offset_y = 0

    return { "x" : tail["x"] + offset_x, "y" : tail["y"] + offset_y }

with open("input.txt", "r") as f:
    motions = f.read().splitlines()

movements = { "R" : { "x" : 1, "y" : 0 }, "L" : { "x" : -1, "y" : 0 }, "U" : { "x" : 0, "y" : 1 }, "D" : { "x" : 0, "y" : -1 } }
head = { "x" : 0, "y" : 0 }
tail = { "x" : 0, "y" : 0 }
positions = [tail]

for motion in motions:
    direction, steps = motion.split(" ")
    for _ in range(int(steps)):
        head["x"] += movements[direction]["x"]
        head["y"] += movements[direction]["y"]
        if not are_touching(head, tail):
            tail = update_tail(head, tail)
            if tail not in positions:
                positions.append(tail)

print(len(positions))