f = open("input.txt", "r")
lines = f.readlines()
f.close()

passports = ()
passport = {}

for line in lines:
    if line == "\n":
        passports += (passport,)
        passport = {}
    elif line == lines[-1]:
        for field in line.strip().split():
            passport[field.split(":")[0]] = field.split(":")[1]
        passports += (passport,)
    else:
        for field in line.strip().split():
            passport[field.split(":")[0]] = field.split(":")[1]

cont = 0

for passport in passports:
    if len(passport) < 7 or (len(passport) == 7 and "cid" in passport):
        continue
    elif len(passport["byr"]) != 4 or not 1920 <= int(passport["byr"]) <= 2002:
        continue
    elif len(passport["iyr"]) != 4 or not 2010 <= int(passport["iyr"]) <= 2020:
        continue
    elif len(passport["eyr"]) != 4 or not 2020 <= int(passport["eyr"]) <= 2030:
        continue
    elif not (passport["hgt"][-2:] == "cm" or passport["hgt"][-2:] == "in"):
        continue
    elif passport["hgt"][-2:] == "cm" and not 150 <= int(passport["hgt"][:-2]) <= 193:
        continue
    elif passport["hgt"][-2:] == "in" and not 59 <= int(passport["hgt"][:-2]) <= 76:
        continue
    elif len(passport["hcl"]) != 7 or passport["hcl"][0] != "#":
        continue
    elif not (passport["ecl"] == "amb" or passport["ecl"] == "blu" or passport["ecl"] == "brn" or passport["ecl"] == "gry" or passport["ecl"] == "grn" or passport["ecl"] == "hzl" or passport["ecl"] == "oth"):
        continue
    elif len(passport["pid"]) != 9:
        continue

    valid = True

    for char in passport["hcl"][1:]:
        if not (ord("0") <= ord(char) <= ord("9") or ord("a") <= ord(char) <= ord("f")):
            valid = False

    for num in passport["pid"]:
        if not ord("0") <= ord(num) <= ord("9"):
            valid = False

    if not valid:
        continue

    cont += 1

print(cont)