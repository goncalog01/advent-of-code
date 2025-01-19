with open("input.txt", "r") as f:
    lines = f.read().splitlines()

nums = lines[0].split(":")[1]
times = [int(x) for x in nums.split(" ") if len(x) > 0]
nums = lines[1].split(":")[1]
distances = [int(x) for x in nums.split(" ") if len(x) > 0]

total = 1
"""
for i in range(len(times)):
    wins = 0
    for n in range(times[i] // 2 + 1):
        if n * (times[i] - n) > distances[i]:
            wins += 1
    if times[i] % 2 == 0:
        wins = (wins - 1) * 2 + 1
    else:
        wins *= 2
    total *= wins
"""
for i in range(len(times)):
    wins = 0
    for n in range(times[i] // 2, -1, -1):
        if n * (times[i] - n) > distances[i]:
            wins += 1
        else:
            break
    if times[i] % 2 == 0:
        wins = (wins - 1) * 2 + 1
    else:
        wins *= 2
    total *= wins

print(total)