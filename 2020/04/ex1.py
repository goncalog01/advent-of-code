f = open("input.txt", "r")
lines = f.readlines()
f.close()

passports = ()
passport = ""

for line in lines:
    if line == "\n":
        passports += (passport[:-1],)
        passport = ""
    elif line == lines[-1]:
        passport += line.strip()
        passports += (passport,)
    else:
        passport += line.strip()
        passport += " "

cont = 0

for passport in passports:
    if len(passport.split()) == 8 or (len(passport.split()) == 7 and passport.find("cid") == -1):
        cont += 1

print(cont)