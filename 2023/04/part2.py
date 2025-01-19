with open("input.txt", "r") as f:
    lines = f.read().splitlines()

instances = [1 for _ in range(len(lines))]
for i in range(len(lines)):
    card = lines[i].split(": ")[1]
    left, right = card.split(" | ")
    winning_nums = [int(x) for x in left.split(" ") if len(x) > 0]
    my_nums = [int(x) for x in right.split(" ") if len(x) > 0]
    winning = len(set(winning_nums) & set(my_nums))
    for n in range(1, winning + 1):
        instances[i + n] += instances[i]

print(sum(instances))