with open("input.txt", "r") as f:
    input = [x.split() for x in f.read().splitlines()]

solution = [int(x) for x in input[0]]

for line in input[1:-1]:
    for i in range(len(line)):
        if input[-1][i] == "+":
            solution[i] += int(line[i])
        else:
            solution[i] *= int(line[i])

print(sum(solution))