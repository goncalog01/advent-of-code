with open("input.txt", "r") as f:
    lines = f.read().splitlines()

start_found = False
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            start = (x, y)
            start_found = True
            break
    if start_found:
        break

if start[1] > 0 and lines[start[1] - 1][start[0]] in ("|", "7", "F"):
    current = (start[0], start[1] - 1)
elif start[1] < len(lines) - 1 and lines[start[1] + 1][start[0]] in ("|", "L", "J"):
    current = (start[0], start[1] + 1)
elif start[0] > 0 and lines[start[1]][start[0] - 1] in ("-", "L", "F"):
    current = (start[0] - 1, start[1])
elif start[0] < len(lines[0]) - 1 and lines[start[1]][start[0] + 1] in ("-", "J", "7"):
    current = (start[0] + 1, start[1])

prev = start
path = [current]
while current != start:
    match lines[current[1]][current[0]]:
        case "|":
            if current[1] > 0 and (current[0], current[1] - 1) != prev:
                prev = current
                current = (current[0], current[1] - 1)
                path.append(current)
            elif current[1] < len(lines) - 1 and (current[0], current[1] + 1) != prev:
                prev = current
                current = (current[0], current[1] + 1)
                path.append(current)
        case "-":
            if current[0] > 0 and (current[0] - 1, current[1]) != prev:
                prev = current
                current = (current[0] - 1, current[1])
                path.append(current)
            elif current[0] < len(lines[0]) - 1 and (current[0] + 1, current[1]) != prev:
                prev = current
                current = (current[0] + 1, current[1])
                path.append(current)
        case "L":
            if current[1] > 0 and (current[0], current[1] - 1) != prev:
                prev = current
                current = (current[0], current[1] - 1)
                path.append(current)
            elif current[0] < len(lines[0]) - 1 and (current[0] + 1, current[1]) != prev:
                prev = current
                current = (current[0] + 1, current[1])
                path.append(current)
        case "J":
            if current[1] > 0 and (current[0], current[1] - 1) != prev:
                prev = current
                current = (current[0], current[1] - 1)
                path.append(current)
            elif current[0] > 0 and (current[0] - 1, current[1]) != prev:
                prev = current
                current = (current[0] - 1, current[1])
                path.append(current)
        case "7":
            if current[1] < len(lines) - 1 and (current[0], current[1] + 1) != prev:
                prev = current
                current = (current[0], current[1] + 1)
                path.append(current)
            elif current[0] > 0 and (current[0] - 1, current[1]) != prev:
                prev = current
                current = (current[0] - 1, current[1])
                path.append(current)
        case "F":
            if current[0] < len(lines[0]) - 1 and (current[0] + 1, current[1]) != prev:
                prev = current
                current = (current[0] + 1, current[1])
                path.append(current)
            elif current[1] < len(lines) - 1 and (current[0], current[1] + 1) != prev:
                prev = current
                current = (current[0], current[1] + 1)
                path.append(current)

print(len(path) // 2)