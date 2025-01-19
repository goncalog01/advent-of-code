with open("input.txt", "r") as f:
    entries = f.read().splitlines()

lengths = (2, 3, 4, 7)
digits = 0

for entry in entries:
    output_value = entry.split(" | ")[1]

    for digit in output_value.split(" "):
        if len(digit) in lengths:
            digits += 1

print(digits)