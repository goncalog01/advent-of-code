def get_loop_size(key):
    value = 1
    i = 1

    while True:
        value *= 7
        value %= 20201227

        if value == key:
            break

        i += 1

    return i

def get_encryption_key(subject_number, loop_size):
    value = 1

    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227

    return value


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

card_key = int(lines[0])
door_key = int(lines[1])

door_loop_size = get_loop_size(door_key)

print(get_encryption_key(card_key, door_loop_size))