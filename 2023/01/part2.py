with open("input.txt", "r") as f:
    lines = f.read().splitlines()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

num_to_dig = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

values = []
for line in lines:
    first_indexes = {}
    last_indexes = {}
    for number in numbers:
        first = line.find(number)
        last = line.rfind(number)
        if first != -1:
           first_indexes[number] = first
        last_indexes[number] = last
    first_dig = min(first_indexes, key=first_indexes.get)
    last_dig = max(last_indexes, key=last_indexes.get)
    if first_dig in num_to_dig:
        first_dig = num_to_dig[first_dig]
    if last_dig in num_to_dig:
        last_dig = num_to_dig[last_dig]
    values.append(first_dig + last_dig)

total = 0
for value in values:
    total += int(value)
print(total)