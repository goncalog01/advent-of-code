with open("input.txt", "r") as f:
    datastream = f.read()

for i in range(3, len(datastream)):
    if len(set(datastream[i-3:i+1])) == 4:
        print(i + 1)
        break