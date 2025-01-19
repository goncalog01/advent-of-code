with open("input.txt", "r") as f:
    measures = [int(x) for x in f.read().splitlines()]

increases = 0

for i in range(1, len(measures)):
    if measures[i-1] < measures[i]:
        increases += 1

print(increases)