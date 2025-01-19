def run(program):
    acc = 0
    i = 0
    instructions = ()
    num_instructions = len(program)

    while True:
        if i in instructions or i > num_instructions or i < 0:
            return -1
        elif i == num_instructions:
            return acc
        op = program[i].split()[0]
        if op == "nop":
            instructions += (i,)
            i += 1
        elif op == "acc":
            acc += int(program[i].split()[1])
            instructions += (i,)
            i += 1
        elif op == "jmp":
            instructions += (i,)
            i += int(program[i].split()[1])

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

i = 0
num_lines = len(lines)

while i < num_lines:
    copy = lines.copy()
    op = lines[i].split()[0]
    if op == "nop":
        copy[i] = copy[i].replace("nop", "jmp")
    elif op == "jmp":
        copy[i] = copy[i].replace("jmp", "nop")
    acc = run(copy)
    if acc >= 0:
        print(acc)
        break
    i += 1