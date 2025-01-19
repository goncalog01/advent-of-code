f = open("input.txt", "r")
nums = f.read().splitlines()
f.close()

prev_nums = []
i = 0

for num in nums:
    valid = False

    if len(prev_nums) < 25:
        prev_nums += [int(num)]
        i = (i + 1) % 25
        continue

    j = 1

    for x in prev_nums:
        for y in prev_nums[j:]:
            if x + y == int(num):
                prev_nums[i] = int(num)
                valid = True
                i = (i + 1) % 25
                break
        if valid:
            break
        j += 1

    if not valid:
        print(num)
        break