f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

nums = []

for line in lines:
    nums += [int(line)]

nums += [0, max(nums) + 3]

nums.sort()

diff1 = 0
diff3 = 0
prev = 0
i = 0
num_lines = len(nums)

while i < num_lines - 1:
    if nums[i + 1] - nums[i] == 1:
        diff1 += 1
    elif nums[i + 1] - nums[i] == 3:
        diff3 += 1
    i += 1

print(diff1 * diff3)