import statistics

with open("input.txt", "r") as f:
    positions = [int(x) for x in f.read().split(",")]

aligned_position = int(statistics.mean(positions))

fuel = 0

for position in positions:
    lower = min(position, aligned_position)
    upper = max(position, aligned_position)

    j = 0

    for i in range(lower, upper):
        j += 1
        fuel += j

print(fuel)