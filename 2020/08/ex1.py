f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

acc = 0
i = 0
instructions = ()
num_lines = len(lines)

while i < num_lines:
    if i in instructions:
        break
    op = lines[i].split()[0]
    if op == "nop":
        instructions += (i,)
        i += 1
    elif op == "acc":
        acc += int(lines[i].split()[1])
        instructions += (i,)
        i += 1
    elif op == "jmp":
        instructions += (i,)
        i += int(lines[i].split()[1])

print(acc)