stones = []
with open("input.txt") as file:
    for line in file:
        for stone in line.strip().split():
            stones.append(stone)

for i in range(75):
    newStones = []
    for stone in stones:
        if stone == "0":
            newStones.append("1")
        elif len(stone) % 2 == 0:
            newStones.append(str(int(stone[:int(len(stone)/2)])))
            newStones.append(str(int(stone[int(len(stone)/2):])))
        else:
            newStones.append(str(int(stone) * 2024))
    stones = newStones

print(len(stones))