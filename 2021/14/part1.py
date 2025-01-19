with open("input.txt", "r") as f:
    input = f.read().splitlines()

template = input[0]
rules = {}

for i in range(2, len(input)):
    x, y = input[i].split(" -> ")
    rules[x] = y

pairs = {}

for i in range(len(template) - 1):
    if template[i] + template[i+1] in pairs:
        pairs[template[i] + template[i+1]] += 1
    else:
        pairs[template[i] + template[i+1]] = 1

for _ in range(10):
    new_pairs = pairs.copy()
    for pair in pairs:
        if pair in rules:
            count = pairs[pair]
            if pair[0] + rules[pair] in new_pairs:
                new_pairs[pair[0] + rules[pair]] += count
            else:
                new_pairs[pair[0] + rules[pair]] = count

            if rules[pair] + pair[1] in new_pairs:
                new_pairs[rules[pair] + pair[1]] += count
            else:
                new_pairs[rules[pair] + pair[1]] = count

            new_pairs[pair] -= count
    pairs = new_pairs.copy()

letters = {}

letters[template[0]] = 1
letters[template[-1]] = 1

for pair in pairs:
    for letter in pair:
        if letter in letters:
            letters[letter] += pairs[pair]
        else:
            letters[letter] = pairs[pair]

print((max(letters.values()) - min(letters.values()))//2)