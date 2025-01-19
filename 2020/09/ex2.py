def weakness(nums, range, inv_num):
    i = 0
    j = range
    len_nums = len(nums)

    while j < len_nums:
        sum = 0
        for n in nums[i:j]:
            sum += n
        if sum == inv_num:
            return min(nums[i:j]) + max(nums[i:j])
        i += 1
        j += 1

    return -1
        

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

nums = []

for line in lines:
    nums += [int(line)]

i = 2
len_nums = len(nums)

while i <= len_nums:
    res = weakness(nums, i, 542529149)
    if res >= 0:
        print(res)
        break
    i += 1