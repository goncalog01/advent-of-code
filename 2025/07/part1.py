with open("input.txt", "r") as f:
    input = f.read().splitlines()

beams = {input[0].find("S")}
total = 0
for line in input[1:]:
    remove = []
    add = []
    for beam in beams:
        if line[beam] == "^":
            total += 1
            remove.append(beam)
            if beam - 1 >= 0:
                add.append(beam - 1)
            if beam + 1 < len(line):
                add.append(beam + 1)
    for beam in remove:
        beams.remove(beam)
    for beam in add:
        beams.add(beam)

print(total)