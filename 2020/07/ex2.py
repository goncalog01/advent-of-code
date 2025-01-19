def num_bags_inside(rules, bag):
    sum = 0
    for rule in rules:
        name = rule.split()[0] + " " + rule.split()[1]
        if name == bag:
            desc = ""
            for word in rule.split()[2:]:
                desc += word + " "
            desc = desc[:-1]
            for i in range(len(desc.split())):
                if desc.split()[i].isdigit():
                    inside_bag = desc.split()[i + 1] + " " + desc.split()[i + 2]
                    sum += int(desc.split()[i]) + int (desc.split()[i]) * num_bags_inside(rules, inside_bag)
    return sum


f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()
print(num_bags_inside(lines, "shiny gold"))