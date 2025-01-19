with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    card = line.split(": ")[1]
    left, right = card.split(" | ")
    winning_nums = [int(x) for x in left.split(" ") if len(x) > 0]
    my_nums = [int(x) for x in right.split(" ") if len(x) > 0]
    winning = len(set(winning_nums) & set(my_nums))
    if winning > 0:
        total += 2**(winning - 1)

print(total)