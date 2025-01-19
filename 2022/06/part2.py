with open("input.txt", "r") as f:
    datastream = f.read()

for i in range(13, len(datastream)):
    if len(set(datastream[i-13:i+1])) == 14:
        print(i + 1)
        break