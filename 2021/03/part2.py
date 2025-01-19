with open("input.txt", "r") as f:
    numbers = f.read().splitlines()

oxygen_nums = numbers.copy()

freq = [0, 0]

for i in range(len(numbers[0])):
    for number in oxygen_nums:
        freq[int(number[i])] += 1

    if freq[0] <= freq[1]:
        most_freq_bit = "1"
    else:
        most_freq_bit = "0"

    temp = oxygen_nums.copy()

    for number in oxygen_nums:
        if number[i] != most_freq_bit:
            temp.remove(number)

    oxygen_nums = temp.copy()

    if len(oxygen_nums) == 1:
        break

    freq = [0, 0]

co2_nums = numbers.copy()

freq = [0, 0]

for i in range(len(numbers[0])):
    for number in co2_nums:
        freq[int(number[i])] += 1

    if freq[0] <= freq[1]:
        least_freq_bit = "0"
    else:
        least_freq_bit = "1"

    temp = co2_nums.copy()

    for number in co2_nums:
        if number[i] != least_freq_bit:
            temp.remove(number)

    co2_nums = temp.copy()

    if len(co2_nums) == 1:
        break

    freq = [0, 0]

print(int(oxygen_nums[0], 2) * int(co2_nums[0], 2))