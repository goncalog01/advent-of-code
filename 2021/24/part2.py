with open("input.txt", "r") as f:
    input = f.read().splitlines()

program = [line.split() for line in input]
model = [1] * 14
stack = []

for i in range(14):
    div, chk, add = map(int, [program[i * 18 + x][-1] for x in [4, 5, 15]])
    if div == 1:
        stack.append((i, add))
    elif div == 26:
        j, add = stack.pop()
        model[i] = model[j] + add + chk
        if model[i] < 1:
            model[j] += 1 - model[i]
            model[i] = 1
    
print("".join(map(str, model)))