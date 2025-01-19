with open("input.txt", "r") as f:
    rucksacks = f.read().splitlines()

priorities_sum = 0

for i in range(0, len(rucksacks), 3):
    rucksack1 = rucksacks[i]
    rucksack2 = rucksacks[i + 1]
    rucksack3 = rucksacks[i + 2]
    common_items = set(rucksack1).intersection(rucksack2).intersection(rucksack3)
    for item in common_items:
        if item.islower():
            priorities_sum += ord(item) - ord('a') + 1
        else:
            priorities_sum += ord(item) - ord('A') + 27

print(priorities_sum)