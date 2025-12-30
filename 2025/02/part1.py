with open("input.txt", "r") as f:
    input = f.read()

ranges = input.split(",")
invalid = 0

for r in ranges:
    min_id, max_id = map(int, r.split("-"))
    for i in range(min_id, max_id + 1):
        id = str(i)
        if len(id) % 2 == 0 and id[:len(id) // 2] == id[len(id) // 2:]:
            invalid += int(id)

print(invalid)