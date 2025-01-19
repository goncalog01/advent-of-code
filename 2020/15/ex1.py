with open("input.txt", "r") as f:
    input = [x for x in f.read().split(",")]

i = 1
nums = {}

for x in input[:-1]:
    nums[int(x)] = i
    i += 1

prev = int(input[-1])
i += 1

while i <= 2020:
    if prev not in nums:
        nums[prev] = i - 1
        prev = 0
    else:
        age = i - 1 - nums[prev]
        nums[prev] = i - 1
        prev = age
    i += 1

print(prev)