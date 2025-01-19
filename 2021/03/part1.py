with open("input.txt", "r") as f:
    numbers = f.read().splitlines()

freq = [[0, 0] for i in range(len(numbers[0]))]

for number in numbers:
    for i in range(len(number)):
        freq[i][int(number[i])] += 1

gamma = ""

for pos in freq:
    if pos[0] < pos[1]:
        gamma += "1"
    else:
        gamma += "0"

epsilon = ""

for bit in gamma:
    if bit == "0":
        epsilon += "1"
    else:
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))