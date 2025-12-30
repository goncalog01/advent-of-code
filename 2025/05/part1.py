with open("input.txt", "r") as f:
    input = f.read().splitlines()

fresh = []

for i in range(len(input)):
    if input[i] == "":
        available = input[i+1:]
        break
    fresh.append(input[i])

total = 0

for ingredient in available:
    for range in fresh:
        min_id, max_id = map(int, range.split("-"))
        if min_id <= int(ingredient) <= max_id:
            total += 1
            break

print(total)