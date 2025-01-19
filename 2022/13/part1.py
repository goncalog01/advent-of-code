RIGHT = 1
WRONG = -1
CONTINUE = 0

def right_order(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return RIGHT
        elif p1 > p2:
            return WRONG
        else:
            return CONTINUE
    elif isinstance(p1, list) and isinstance(p2, list):
        l1 = len(p1)
        l2 = len(p2)
        if l1 != 0 and l2 == 0:
            return WRONG
        elif l1 == 0 and l2 != 0:
            return RIGHT
        elif l1 == 0 and l2 == 0:
            return CONTINUE

        r = right_order(p1[0], p2[0])
        if r == RIGHT:
            return RIGHT
        elif r == WRONG:
            return WRONG
        else:
            return right_order(p1[1:], p2[1:])
    elif isinstance(p1, int):
        return right_order([p1], p2)
    elif isinstance(p2, int):
        return right_order(p1, [p2])

with open("input.txt", "r") as f:
    packets = f.read().splitlines()

sum = 0
for i in range(0, len(packets), 3):
    p1 = eval(packets[i])
    p2 = eval(packets[i+1])
    if right_order(p1, p2) == RIGHT:
        sum += i // 3 + 1
print(sum)