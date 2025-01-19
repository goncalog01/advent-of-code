def value_of(monkeys, monkey):
    if monkeys[monkey].isdigit():
        return int(monkeys[monkey])
    else:
        tokens = monkeys[monkey].split(" ")
        if tokens[1] == "+":
            return value_of(monkeys, tokens[0]) + value_of(monkeys, tokens[2])
        elif tokens[1] == "-":
            return value_of(monkeys, tokens[0]) - value_of(monkeys, tokens[2])
        elif tokens[1] == "*":
            return value_of(monkeys, tokens[0]) * value_of(monkeys, tokens[2])
        elif tokens[1] == "/":
            return value_of(monkeys, tokens[0]) / value_of(monkeys, tokens[2])

with open("input.txt", "r") as f:
    data = f.read().splitlines()

monkeys = dict()

for line in data:
    monkey, yell = line.split(": ")
    monkeys[monkey] = yell

print(int(value_of(monkeys, "root")))