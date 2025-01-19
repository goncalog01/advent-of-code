import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

i = 0
for line in data:
    if line == "":
        break
    i += 1

stacks = { str(x) : [] for x in data[i-1].strip().split("   ") }

for y in range(1, len(stacks) * 4 - 2, 4):
    for x in range(i - 1):
        if data[x][y].isupper():
            stacks[str((y + 3) // 4)].insert(0, data[x][y])

for line in data[i+1:]:
    nums = re.findall(r'\d+', line)
    stacks[nums[2]].extend(stacks[nums[1]][-int(nums[0]):])
    for _ in range(int(nums[0])):
        stacks[nums[1]].pop()

message = ""
for stack in stacks.values():
    message += stack[-1]

print(message)