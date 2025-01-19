with open("input.txt", "r") as f:
    input = f.read().strip()

cups = []

for n in input:
    cups += [int(n)]

current_cup = cups[0]

for i in range(100):
    pick_up = []
    for j in range(1, 4):
        pick_up += [cups[(cups.index(current_cup) + j) % len(cups)]]
    dest = current_cup - 1
    if dest == 0:
        dest = 9
    while dest in pick_up:
        dest -= 1
        if dest == 0:
            dest = 9
    for cup in pick_up:
        cups.remove(cup)
    cups = cups[:cups.index(dest) + 1] + pick_up + cups[cups.index(dest) + 1:]
    current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]

labels = ""

for i in range(1, 9):
    labels += str(cups[(cups.index(1) + i) % len(cups)])

print(labels)