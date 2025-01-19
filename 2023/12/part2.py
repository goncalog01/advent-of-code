from functools import cache

@cache
def count_arrangements(springs_list):
    springs = springs_list[0]
    groups = springs_list[1]
    count = 0
    if len(groups) == 0:
        if "#" in springs:
            return 0
        else:
            return 1
    if len(springs) < groups[0]:
        return 0
    if "." not in springs[:groups[0]] and (len(springs) == groups[0] or springs[groups[0]] != "#"):
        count += count_arrangements((springs[groups[0] + 1:], groups[1:]))
    if springs[0] != "#":
        count += count_arrangements((springs[1:], groups))
    return count

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

records = []
for line in lines:
    springs, nums = line.split(" ")
    groups = [int(x) for x in nums.split(",")]
    springs_unfolded = ""
    for _ in range(5):
        springs_unfolded += springs + "?"
    records.append((springs_unfolded[:-1], tuple(groups * 5)))

total = 0
for row in records:
    total += count_arrangements(row)

print(total)