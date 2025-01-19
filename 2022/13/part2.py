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

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        r = right_order(array[j], pivot)
        if r == RIGHT or r == CONTINUE:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quick_sort(array, low, high):
    if right_order(low, high) == RIGHT:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

with open("input.txt", "r") as f:
    data = f.read().splitlines()

packets = []
for line in data:
    if line == "":
        continue
    else:
        packets.append(eval(line))
packets.extend([[[2]], [[6]]])
quick_sort(packets, 0, len(packets) - 1)
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))