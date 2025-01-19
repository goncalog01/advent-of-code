with open("input.txt", "r") as f:
    program = f.read().splitlines()

cycles = (20, 60, 100, 140, 180, 220)
x = 1
values = []

for line in program:
    instr = line.split(" ")
    if instr[0] == "noop":
        values.append(x)
    else:
        values.append(x)
        values.append(x)
        x += int(instr[1])

sum_signal_strengths = 0

for cycle in cycles:
    sum_signal_strengths += cycle * values[cycle - 1]

print(sum_signal_strengths)