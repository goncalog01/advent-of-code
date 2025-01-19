with open("input.txt", "r") as f:
    lines = f.read().splitlines()

matches = { "(" : ")", "[" : "]", "{" : "}", "<" : ">" }
points = { ")" : 1, "]" : 2, "}" : 3, ">" : 4 }

scores = []

for line in lines:
    stack = []
    incomplete = True

    for char in line:
        if char in matches:
            stack += [char]
        else:
            if char != matches[stack.pop()]:
                incomplete = False
                break

    if not incomplete:
        continue

    line_score = 0

    while stack != []:
        line_score *= 5
        line_score += points[matches[stack.pop()]]

    scores += [line_score]

scores.sort()
print(scores[len(scores) // 2])