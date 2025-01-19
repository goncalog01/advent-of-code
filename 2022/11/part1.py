import re

class Monkey:
    def __init__(self, items, op, test, true, false):
        self.items = items
        self.op = op
        self.test = test
        self.true = true
        self.false = false
        self.inspected = 0

    def do_op(self, worry):
        if self.op[1].isdigit():
            arg = int(self.op[1])
        elif self.op[1] == "old":
            arg = worry

        if self.op[0] == "+":
            return worry + arg
        elif self.op[0] == "*":
            return worry * arg

    def do_test(self, worry):
        if worry % self.test == 0:
            return self.true
        else:
            return self.false

    def inspect_item(self, worry):
        worry_lvl = self.do_op(worry) // 3
        return (worry_lvl, self.do_test(worry_lvl))

    def add_items(self, items):
        self.items.extend(items)

    def num_inspected(self):
        return self.inspected

    def do_round(self):
        throw = dict()
        for item in self.items:
            to_throw = self.inspect_item(item)
            self.inspected += 1
            if to_throw[1] in throw:
                throw[to_throw[1]].append(to_throw[0])
            else:
                throw[to_throw[1]] = [to_throw[0]]
        self.items.clear()
        return throw

with open("input.txt", "r") as f:
    data = [x.strip() for x in f.read().splitlines()]

monkeys = dict()

for i in range(0, len(data), 7):
    id = int(re.findall(r'\d+', data[i])[0])
    items = [int(x) for x in re.findall(r'\d+', data[i+1])]
    op = data[i+2].split(" ")[-2:]
    test = int(data[i+3].split(" ")[-1])
    true = int(data[i+4].split(" ")[-1])
    false = int(data[i+5].split(" ")[-1])
    monkeys[id] = Monkey(items, op, test, true, false)

for _ in range(20):
    for i in range(len(monkeys)):
        throw = monkeys[i].do_round()
        for m in throw:
            monkeys[m].add_items(throw[m])

most_inspected = [0, 0]
for monkey in monkeys.values():
    if monkey.num_inspected() > most_inspected[0]:
        most_inspected[0] = monkey.num_inspected()
        most_inspected.sort()

print(most_inspected[0] * most_inspected[1])