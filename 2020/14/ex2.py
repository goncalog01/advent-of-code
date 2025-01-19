def apply_mask(mask, n):
    binary = "0" * (36 - len(bin(n)[2:])) + bin(n)[2:]
    for i in range(len(mask)):
        if mask[i] == "0":
            continue
        new_binary = list(binary)
        new_binary[i] = mask[i]
        binary = "".join(new_binary)

    addrs = ()

    for addr in replaceX(binary):
        if int(addr, 2) not in addrs:
            addrs += (int(addr, 2),)
    
    return addrs

def replaceX(n):
    len_n = len(n)
    i = 0
    while i < len_n:
        if n[i] == "X":
            new0 = list(n)
            new0[i] = "0"
            new0 = "".join(new0)
            new1 = list(n)
            new1[i] = "1"
            new1 = "".join(new1)
            return replaceX(new0) + replaceX(new1)
        i += 1
    return (n,)


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
        for addr in apply_mask(mask, int(line[0])):
            mem[addr] = int(line[1])

sum = 0

for addr in mem:
    sum += mem[addr]

print(sum)