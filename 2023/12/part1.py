def count_arrangements(springs, groups):
    count = 0
    if len(groups) == 0:
        if "#" in springs:
            return 0
        else:
            return 1
    if len(springs) < groups[0]:
        return 0
    if "." not in springs[:groups[0]] and (len(springs) == groups[0] or springs[groups[0]] != "#"):
        count += count_arrangements(springs[groups[0] + 1:], groups[1:])
    if springs[0] != "#":
        count += count_arrangements(springs[1:], groups)
    return count

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

records = []
for line in lines:
    springs, groups = line.split(" ")
    records.append([springs, [int(x) for x in groups.split(",")]])

total = 0
for row in records:
    total += count_arrangements(row[0], row[1])

print(total)