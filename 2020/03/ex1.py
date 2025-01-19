f = open("input.txt", "r")
lines = f.readlines()
f.close()

rows = ()

for line in lines[:-1]:
    line = line[:-1]
    rows += (line,)

rows += (lines[-1],)

cont = 0
col = 0

for row in rows:
    if row[col] == "#":
        cont += 1
    col = (col + 3) % len(row)

print(cont)