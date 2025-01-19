f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

sum = 0
group = ()

for line in lines:
    if line == "":
        sum += len(group)
        group = ()
    elif line == lines[-1]:
        for char in line:
            if char not in group:
                group += (char,)
        sum += len(group)
    else:
        for char in line:
            if char not in group:
                group += (char,)

print(sum)