with open("input.txt", "r") as f:
    calories = f.read().splitlines()

max_calories = [0, 0, 0]
current_calories = 0

for c in calories:
    if c == "":
        if current_calories > max_calories[0]:
            max_calories[0] = current_calories
            max_calories.sort()
        current_calories = 0
    else:
        current_calories += int(c)

if current_calories > max_calories[0]:
    max_calories[0] = current_calories

print(sum(max_calories))