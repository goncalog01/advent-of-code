f = open("input.txt", "r")
lines = f.readlines()
f.close()

rows = ()

for line in lines[:-1]:
    line = line[:-1]
    rows += (line,)

rows += (lines[-1],)

cont1 = 0
col1 = 0

cont2 = 0
col2 = 0

cont3 = 0
col3 = 0

cont4 = 0
col4 = 0

cont5 = 0
col5 = 0
even = True

for row in rows:
    if row[col1] == "#":
        cont1 += 1
    if row[col2] == "#":
        cont2 += 1
    if row[col3] == "#":
        cont3 += 1
    if row[col4] == "#":
        cont4 += 1
    if even:
        if row[col5] == "#":
            cont5 += 1
        col5 = (col5 + 1) % len(row)
        even = False
    else:
        even = True
    col1 = (col1 + 1) % len(row)
    col2 = (col2 + 3) % len(row)
    col3 = (col3 + 5) % len(row)
    col4 = (col4 + 7) % len(row)

print(cont1 * cont2 * cont3 * cont4 * cont5)