with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    seq = [int(x) for x in line.split(" ")]
    last_vals = []
    while seq.count(0) != len(seq):
        last_vals.append(seq[-1])
        next_seq = []
        for i in range(len(seq) - 1):
            next_seq.append(seq[i + 1] - seq[i])
        seq = next_seq
    total += sum(last_vals)

print(total)