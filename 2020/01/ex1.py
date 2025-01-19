f = open("input.txt", "r")
content = f.readlines()
f.close()
numbers = ()
for line in content:
    n = int(line)
    numbers += (n,)
cont = 1
for x in numbers:
    for y in numbers[cont:]:
        if x + y == 2020:
            print(x * y)
    cont += 1