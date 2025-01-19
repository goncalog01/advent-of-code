def is_subset(subset, set):
    for x in subset:
        in_set = False
        for y in set:
            if x == y:
                in_set = True
                break
        if not in_set:
            return False
    return True

with open("input.txt", "r") as f:
    entries = f.read().splitlines()

sum = 0

for entry in entries:
    signal_patterns, output_value = entry.split(" | ")

    signal_patterns = signal_patterns.split(" ")
    output_value = output_value.split(" ")

    digits = {}

    for pattern in signal_patterns:
        length = len(pattern)

        if "1" not in digits and length == 2:
            digits["1"] = pattern
        elif "7" not in digits and length == 3:
            digits["7"] = pattern
        elif "4" not in digits and length == 4:
            digits["4"] = pattern
        elif "8" not in digits and length == 7:
            digits["8"] = pattern

    for pattern in signal_patterns:
        if len(pattern) == 6:
            if "9" not in digits and is_subset(digits["4"], pattern):
                digits["9"] = pattern
            elif "0" not in digits and is_subset(digits["7"], pattern):
                digits["0"] = pattern
            else:
                digits["6"] = pattern

    for pattern in signal_patterns:
        if len(pattern) == 5:
            if "3" not in digits and is_subset(digits["7"], pattern):
                digits["3"] = pattern
            elif "5" not in digits and is_subset(pattern, digits["6"]):
                digits["5"] = pattern
            else:
                digits["2"] = pattern

    output = ""

    for pattern in output_value:
        for digit in digits:
            if len(pattern) == len(digits[digit]) and is_subset(digits[digit], pattern):
                output += digit
                break

    sum += int(output)

print(sum)