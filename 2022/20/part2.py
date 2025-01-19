with open("input.txt", "r") as f:
    data = f.read().splitlines()

sequence = []
occurrences = dict()
for line in data:
    n = int(line) * 811589153
    if n in occurrences:
        occurrences[n] += 1
    else:
        occurrences[n] = 1
    sequence.append([n, occurrences[n]])

l = len(sequence)
new_sequence = sequence.copy()
for _ in range(10):
    for n in sequence:
        if n[0] != 0:
            i = new_sequence.index(n)
            new_sequence.remove(n)
            new_sequence.insert((i + n[0]) % (l - 1), n)

print(sum(new_sequence[(new_sequence.index([0, 1]) + i) % l][0] for i in (1000, 2000, 3000)))