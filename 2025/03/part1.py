with open("input.txt", "r") as f:
    batteries = f.read().splitlines()

def highest_joltage_between(bank, start, finish):
    highest = int(bank[start])
    index = start

    for i in range(start + 1, finish):
        if int(bank[i]) > highest:
            highest = int(bank[i])
            index = i

    return str(highest), index

digits = 2
total = 0

for bank in batteries:
    output = ""
    index = -1
    for i in range(digits):
        digit, index = highest_joltage_between(bank, index + 1, len(bank) - (digits - i - 1))
        output += digit
    total += int(output)

print(total)