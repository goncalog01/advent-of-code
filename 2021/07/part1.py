import statistics

with open("input.txt", "r") as f:
    positions = [int(x) for x in f.read().split(",")]

aligned_position = int(statistics.median(positions))

fuel = 0

for position in positions:
    fuel += abs(position - aligned_position)

print(fuel)