f = open("input.txt", "r")
lines = f.readlines()
f.close()

passwords = ()

for line in lines:
    n = ""
    cont = 0
    while line[cont] != "-":
        n += line[cont]
        cont += 1
    min = int(n)
    n = ""
    cont += 1
    while line[cont] != " ":
        n += line[cont]
        cont += 1
    max = int(n)
    cont += 1
    letter = line[cont]
    cont += 3
    password = line[cont:]
    passwords += ((min, max, letter, password),)

cont = 0

for password in passwords:
    contl = 0
    for l in password[3]:
        if l == password[2]:
            contl += 1
    if password[0] <= contl <= password[1]:
        cont += 1

print(cont)