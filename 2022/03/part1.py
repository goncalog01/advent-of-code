with open("input.txt", "r") as f:
    rucksacks = f.read().splitlines()

priorities_sum = 0

for rucksack in rucksacks:
    mid = len(rucksack) // 2
    comp1 = rucksack[:mid]
    comp2 = rucksack[mid:]
    common_items = set(comp1).intersection(comp2)
    for item in common_items:
        if item.islower():
            priorities_sum += ord(item) - ord('a') + 1
        else:
            priorities_sum += ord(item) - ord('A') + 27

print(priorities_sum)