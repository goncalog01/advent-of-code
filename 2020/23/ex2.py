def crab_cups(cycle, n):
    cur_val = cycle[0]
    max_val = max(cycle)

    cycle_dict = dict(zip(cycle, cycle[1:]))
    cycle_dict[cycle[-1]] = cycle[0]

    def pick_up(n):
        pick = [cycle_dict[cur_val]]
        for _ in range(n - 1):
            pick.append(cycle_dict[pick[-1]])
        return pick

    for r in range(n):
        pick = pick_up(3)

        next_val = cur_val-1
        while next_val <= 0 or next_val in pick:
            next_val -= 1
            if next_val <= 0:
                next_val = max_val

        cycle_dict[cur_val] = cycle_dict[pick[-1]]
        cycle_dict[pick[-1]] = cycle_dict[next_val]
        cycle_dict[next_val] = pick[0]

        cur_val = cycle_dict[cur_val]

    return cycle_dict

with open("input.txt", "r") as f:
    input = f.read().strip()

cups = []

for n in input:
    cups += [int(n)]

cups += [i for i in range(10, 1000001)]

cycle = crab_cups(cups, 10000000)
v1 = cycle[1]
v2 = cycle[v1]
print(v1 * v2)