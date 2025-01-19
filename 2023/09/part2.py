with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    seq = [int(x) for x in line.split(" ")]
    first_vals = []
    while seq.count(0) != len(seq):
        first_vals.append(seq[0])
        next_seq = []
        for i in range(len(seq) - 1):
            next_seq.append(seq[i + 1] - seq[i])
        seq = next_seq
    curr = 0
    for i in range(len(first_vals) - 1, -1, -1):
        curr = first_vals[i] - curr
    total += curr

print(total)