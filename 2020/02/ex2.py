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
    pos1 = int(n)
    n = ""
    cont += 1
    while line[cont] != " ":
        n += line[cont]
        cont += 1
    pos2 = int(n)
    cont += 1
    letter = line[cont]
    cont += 3
    password = line[cont:]
    passwords += ((pos1, pos2, letter, password),)

cont = 0

for password in passwords:
    cont_occur = 0
    if password[3][password[0] - 1] == password[2]:
        cont_occur += 1
    if password[3][password[1] - 1] == password[2]:
        cont_occur += 1
    if cont_occur == 1:
        cont += 1

print(cont)