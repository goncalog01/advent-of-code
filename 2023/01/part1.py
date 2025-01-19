with open("input.txt", "r") as f:
    lines = f.read().splitlines()

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
    values.append(first_dig + last_dig)

total = 0
for value in values:
    total += int(value)
print(total)