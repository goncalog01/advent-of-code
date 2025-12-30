import functools

with open("input.txt", "r") as f:
    input = f.read().splitlines()

@functools.cache
def timelines(x, y):
    if y == len(input) - 1:
        return 1
    elif input[y][x] == "^":
        return timelines(x - 1, y + 1) + timelines(x + 1, y + 1)
    else:
        return timelines(x, y + 1)
    
print(timelines(input[0].find("S"), 0))