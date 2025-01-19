def check_horizontal_symmetry(pattern, row1, row2):
    i = row1
    j = row2
    while i >= 0 and j < len(pattern):
        if pattern[i] != pattern[j]:
            return False
        i -= 1
        j += 1
    return True

def search_horizontal_line(pattern):
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1] and check_horizontal_symmetry(pattern, i, i + 1):
            return i
    else:
        return -1
    
def check_vertical_symmetry(pattern, col1, col2):
    i = col1
    j = col2
    while i >= 0 and j < len(pattern[0]):
        column1 = "".join(pattern[k][i] for k in range(len(pattern)))
        column2 = "".join(pattern[k][j] for k in range(len(pattern)))
        if column1 != column2:
            return False
        i -= 1
        j += 1
    return True

def search_vertical_line(pattern):
    for i in range(len(pattern[0]) - 1):
        col1 = "".join(pattern[j][i] for j in range(len(pattern)))
        col2 = "".join(pattern[j][i + 1] for j in range(len(pattern)))
        if col1 == col2 and check_vertical_symmetry(pattern, i, i + 1):
            return i
    else:
        return -1

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

patterns = []
current = []
for line in lines:
    if line == "":
        patterns.append(current)
        current = []
    else:
        current.append(line)
else:
    patterns.append(current)

total = 0
for pattern in patterns:
    res = search_horizontal_line(pattern)
    if res != -1:
        total += 100 * (res + 1)
    res = search_vertical_line(pattern)
    if res != -1:
        total += res + 1

print(total)