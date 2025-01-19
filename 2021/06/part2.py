with open("input.txt", "r") as f:
    fishes = [int(x) for x in f.read().split(",")]

count_ages = { x : 0 for x in range(9) }

for fish in fishes:
    count_ages[fish] += 1

for day in range(256):
    temp = { x : 0 for x in range(9) }

    for age, count in count_ages.items():
        if age > 0:
            temp[age - 1] += count
        else:
            temp[6] += count
            temp[8] += count

    count_ages = temp

print(sum(count_ages.values()))