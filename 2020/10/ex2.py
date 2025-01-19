f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

nums = []

for line in lines:
    nums += [int(line)]

nums += [0, max(nums) + 3]

nums.sort()

pos = 0
num_arrangements = [0 for i in range(len(nums))]
num_arrangements[0] = 1
len_nums = len(nums)

while pos < len_nums:
    for i in range(1, 4):
        if pos - i < 0:
            break
        for j in range(1, 4):
            if nums[pos] - j == nums[pos - i]:
                num_arrangements[pos] += num_arrangements[pos - i]
                break
    pos += 1

print(num_arrangements[-1])