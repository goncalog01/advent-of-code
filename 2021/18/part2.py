import math

def add(x, y):
    return "[" + x + "," + y + "]"

def reduce(n):
    changed = True
    while changed:
        changed = False
        pairs = 0
        i = 0
        s = ""
        found = False
        while i < len(n):
            if n[i] == "[":
                pairs += 1
                if not found and len(s) > 1:
                    found = True
                    end = i - 1
                    start = i - len(s)
                else:
                    s = ""
            elif n[i] == "]":
                pairs -= 1
                if not found and len(s) > 1:
                    found = True
                    end = i - 1
                    start = i - len(s)
                else:
                    s = ""
            elif n[i] == ",":
                if not found and len(s) > 1:
                    found = True
                    end = i - 1
                    start = i - len(s)
                else:
                    s = ""
            else:
                if pairs == 5:
                    n = explode(n, i - 1, n.index("]", i))
                    changed = True
                    break
                s += n[i]
            i += 1
        if found and not changed:
                n = split(n, start, end)
                changed = True
    return n

def explode(n, start, end):
    i = start - 1
    x, y = n[start + 1:end].split(",")
    s = ""
    while i > 0 and not n[i].isdigit():
        i -= 1
    while i > 0 and n[i].isdigit():
        s = n[i] + s
        i -= 1
    if s != "":
        length = len(s)
        s = str(int(s) + int(x))
        res = n[:i+1] + s + n[i+length+1:start]
    else:
        res = n[:start]
    i = end + 1
    s = ""
    while i < len(n) and not n[i].isdigit():
        i += 1
    while i < len(n) and n[i].isdigit():
        s += n[i]
        i += 1
    if s != "":
        length = len(s)
        s = str(int(s) + int(y))
        res += "0" + n[end+1:i-length] + s + n[i:]
    else:
        res += "0" + n[end+1:]
    return res
    
def split(n, start, end):
    x = n[start:end+1]
    s = "[" + str(math.floor(int(x)/2)) + "," + str(math.ceil(int(x)/2)) + "]"
    return n[:start] + s + n[end+1:]

def sum(x, y):
    return reduce(add(x, y))
        
def magnitude(n):
    if isinstance(n, int):
        return n
    else:
        return 3 * magnitude(n[0]) + 2 * magnitude(n[1])

with open("input.txt", "r") as f:
    numbers = f.read().splitlines()

max_magnitude = -math.inf

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i == j:
            continue
        max_magnitude = max(max_magnitude, magnitude(eval(sum(numbers[i], numbers[j]))))

print(max_magnitude)