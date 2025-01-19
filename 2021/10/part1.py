with open("input.txt", "r") as f:
    lines = f.read().splitlines()

matches = { "(" : ")", "[" : "]", "{" : "}", "<" : ">" }
points = { ")" : 3, "]" : 57, "}" : 1197, ">" : 25137 }

score = 0

for line in lines:
    stack = []

    for char in line:
        if char in matches:
            stack += [char]
        else:
            if char != matches[stack.pop()]:
                score += points[char]
                break

print(score)