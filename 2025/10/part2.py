from z3 import *

with open("input.txt", "r") as f:
    input = f.read().splitlines()

def min_presses(machine):
    joltage, buttons = machine
    X = IntVector("x", len(buttons))

    s = Optimize()
    for _ in range(len(buttons)):
        s.add([x >= 0 for x in X])

    A = []
    for button in buttons:
        row = [0 for _ in range(len(joltage))]
        for w in button:
            row[w] = 1
        A.append(row)

    for i in range(len(joltage)):
        s.add(Sum(X[k]*A[k][i] for k in range(len(buttons))) == joltage[i])
    s.minimize(Sum(X))

    if s.check() == sat:
        model = s.model()
        return sum(model[k].as_long() for k in model)

machines = []
for line in input:
    info = line.split(" ")
    joltage = list(map(int, info[-1][1:-1].split(",")))
    buttons = [list(map(int, x[1:-1].split(","))) for x in info[1:-1]]
    machines.append([joltage, buttons])

print(sum(min_presses(m) for m in machines))