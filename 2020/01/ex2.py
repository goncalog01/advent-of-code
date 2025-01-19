f = open("input.txt", "r")
content = f.readlines()
f.close()
numbers = ()
for line in content:
    n = int(line)
    numbers += (n,)
conty = 1
contz = 2
for x in numbers:
    for y in numbers[conty:]:
        for z in numbers[contz:]:
            if x + y + z == 2020:
                print(x * y * z)
        contz += 1
    conty += 1
    contz = conty + 1