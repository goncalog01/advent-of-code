f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

i = 0
bags = ["shiny gold"]

while i < len(bags):
    bag = bags[i]
    for line in lines:
        name = line.split()[0] + " " + line.split()[1]
        desc = ""
        for word in line.split()[2:]:
            desc += word + " "
        desc = desc[:-1]
        if bag in desc and name not in bags:
            bags += [name]
    i += 1

print(len(bags) - 1)