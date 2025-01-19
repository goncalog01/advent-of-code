def solve_simple(expression):
    elements = expression.split()
    res = int(elements[0])
    for i in range(1, len(elements)):
        if elements[i] == "+":
            res += int(elements[i + 1])
        elif elements[i] == "*":
            res *= int(elements[i + 1])
    return res

def solve(expression):
    while "(" in expression or ")" in expression:
        copy = expression
        exp = ""
        new_exp = False
        for i in range(len(expression)):
            if expression[i] == "(":
                exp = expression[i]
                new_exp = True
            elif expression[i] == ")" and new_exp:
                exp += expression[i]
                copy = copy.replace(exp, str(solve_simple(exp[1:-1])))
                exp = ""
                new_exp = False
            else:
                exp += expression[i]
        expression = copy
    return solve_simple(expression)

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

sum = 0

for expression in lines:
    sum += solve(expression)

print(sum)