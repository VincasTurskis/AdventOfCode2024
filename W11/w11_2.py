def applyRule(stone) -> list:
    stoneStr = str(stone)
    newStones = []
    if stone == 0:
        newStones.append(1)
    elif len(stoneStr) % 2 == 0:
        newStones.append(int(stoneStr[:int(len(stoneStr)/2)]))
        newStones.append(int(stoneStr[int(len(stoneStr)/2):]))
    else:
        newStones.append(stone * 2024)
    return newStones


lookup = dict()
counters = dict()
with open("input.txt") as file:
    for line in file:
        for stone in line.strip().split():
            counters[int(stone)] = 1

for i in range(75):
    newCounters = dict()
    for key in counters:
        if key not in lookup:
            lookup[key] = applyRule(key)
        for outcome in lookup[key]:
            if outcome not in newCounters:
                newCounters[outcome] = 0
            newCounters[outcome] += counters[key]
    counters = newCounters
ans = 0
for key in counters:
    ans += counters[key]
print(ans)