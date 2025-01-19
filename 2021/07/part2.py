import statistics

def try_position(pos):
    fuel = 0

    for position in positions:
        lower = min(position, pos)
        upper = max(position, pos)

        j = 0

        for i in range(lower, upper):
            j += 1
            fuel += j

    return fuel

with open("input.txt", "r") as f:
    positions = [int(x) for x in f.read().split(",")]

fuel = min(try_position(int(statistics.mean(positions))), try_position(round(statistics.mean(positions))))

print(fuel)