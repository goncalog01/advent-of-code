from sympy import symbols, solve

def equation(monkeys, monkey):
    if monkey == "humn":
        return monkey
    elif monkeys[monkey].isdigit():
        return monkeys[monkey]
    else:
        tokens = monkeys[monkey].split(" ")
        if tokens[1] == "+":
            return "(" + equation(monkeys, tokens[0]) + " + " + equation(monkeys, tokens[2]) + ")"
        elif tokens[1] == "-":
            return "(" + equation(monkeys, tokens[0]) + " - " + equation(monkeys, tokens[2]) + ")"
        elif tokens[1] == "*":
            return "(" + equation(monkeys, tokens[0]) + " * " + equation(monkeys, tokens[2]) + ")"
        elif tokens[1] == "/":
            return "(" + equation(monkeys, tokens[0]) + " / " + equation(monkeys, tokens[2]) + ")"

with open("input.txt", "r") as f:
    data = f.read().splitlines()

monkeys = dict()

for line in data:
    monkey, yell = line.split(": ")
    if monkey != "humn":
        monkeys[monkey] = yell

left, _, right = monkeys["root"].split(" ")
humn = symbols("humn")
if "humn" in left:
    expr = eval(equation(monkeys, left)) - eval(equation(monkeys, right))
else:
    expr = eval(equation(monkeys, right)) - eval(equation(monkeys, left))
print(int(solve(expr)[0]))