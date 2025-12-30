with open("input.txt", "r") as f:
    input = f.read().splitlines()

intervals = []

for interval in input:
    if interval == "":
        break
    start, end = map(int, interval.split("-"))
    intervals.append((start, end))

intervals = sorted(intervals, key=lambda x: x[0])
merged = []
current_start, current_end = intervals[0]

for start, end in intervals[1:]:
    if start <= current_end:
        current_end = max(current_end, end)
    else:
        merged.append((current_start, current_end))
        current_start, current_end = start, end

merged.append((current_start, current_end))
total = 0

for start, end in merged:
    total += end - start + 1

print(total)