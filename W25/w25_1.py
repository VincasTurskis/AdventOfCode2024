keys = []
locks = []


with open("input.txt") as file:
    line = file.readline()
    while line != "":
        line = line.strip()
        lock = True
        if line == "#####":
            lock = True
        elif line == ".....":
            lock = False
        else:
            print("fuck")
            break
        colHeights = [0, 0, 0, 0, 0]
        while line != "":
            for i in range(5):
                if line[i] == "#":
                    colHeights[i] += 1
            line = file.readline().strip()

        for i in range(5):
            colHeights[i] -= 1
        if lock:
            locks.append(colHeights)
        else:
            keys.append(colHeights)
        line = file.readline()

counter = 0
for key in keys:
    for lock in locks:
        overlap = False
        for i in range(5):
            if key[i] + lock[i] > 5:
                overlap = True
                break
        if not overlap:
            counter += 1

print(counter)
