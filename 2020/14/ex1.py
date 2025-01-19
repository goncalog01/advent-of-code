def apply_mask(mask, n):
    binary = "0" * (36 - len(bin(n)[2:])) + bin(n)[2:]
    for i in range(len(mask)):
        if mask[i] == "X":
            continue
        new_binary = list(binary)
        new_binary[i] = mask[i]
        binary = "".join(new_binary)
    return int(binary, 2)

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

program = ()

for line in lines:
    new_line = line.split(" = ")
    if new_line[0] != "mask":
        new_line[0] = new_line[0].replace("mem[", "").replace("]", "")
    program += (new_line,)

mem = {}

for line in program:
    if line[0] == "mask":
        mask = line[1]
    else:
        mem[line[0]] = apply_mask(mask, int(line[1]))

sum = 0

for addr in mem:
    sum += mem[addr]

print(sum)