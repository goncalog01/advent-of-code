with open("input.txt", "r") as f:
    measures = [int(x) for x in f.read().splitlines()]

increases = 0

for i in range(len(measures) - 3):
    if measures[i] + measures[i+1] + measures[i+2] < measures[i+1] + measures[i+2] + measures[i+3]:
        increases += 1

print(increases)