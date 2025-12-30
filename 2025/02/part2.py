with open("input.txt", "r") as f:
    input = f.read()

ranges = input.split(",")
invalid = 0

for r in ranges:
    min_id, max_id = map(int, r.split("-"))
    for i in range(min_id, max_id + 1):
        id = str(i)
        
        for l in range(1, len(id) // 2 + 1):
            if len(id) % l != 0:
                continue

            if id[:l] * (len(id) // l) == id:
                invalid += int(id)
                break

print(invalid)