with open("input.txt", "r") as f:
    input = f.read().splitlines()

column_sizes = []
space = 0
for c in input[-1][1:]:
    if c == " ":
        space += 1
    else:
        column_sizes.append(space)
        space = 0
column_sizes.append(space + 1)

numbers = [[] for _ in range(len(input) - 1)]
for i in range(len(input) - 1):
    current_index = 0
    for j in range(len(column_sizes)):
        numbers[i].append(input[i][current_index : current_index + column_sizes[j]])
        current_index += column_sizes[j] + 1

problems = []

for i in range(len(numbers[0])):
    problems.append(["" for _ in range(len(numbers[0][i]))])

for line in numbers:
    for i in range(len(line)):
        for j in range(len(line[i])):
            if line[i][j] != " ":
                problems[i][j] += line[i][j]

solutions = []
operators = input[-1].split()
for i in range(len(column_sizes)):
    if operators[i] == "+":
        total = 0
        for n in problems[i]:
            total += int(n)
        solutions.append(total)
    else:
        total = 1
        for n in problems[i]:
            total *= int(n)
        solutions.append(total)

print(sum(solutions))