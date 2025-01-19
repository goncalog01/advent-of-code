f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

sum = 0
group = []
new_group = True

for line in lines:
    if line == "":
        sum += len(group)
        group = []
        new_group = True
    elif new_group and line == lines[-1]:
        sum += len(line)
    elif new_group:
        for char in line:
            group += [char]
        new_group = False
    elif line == lines[-1]:
        copy = group.copy()
        for char in group:
            if char not in line:
                group.remove(char)
        group = copy.copy()
        sum += len(group)
    else:
        copy = group.copy()
        for char in group:
            if char not in line:
                copy.remove(char)
        group = copy.copy()

print(sum)