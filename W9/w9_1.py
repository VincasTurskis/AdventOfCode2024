space = False
disk = []
curInputIndex = 0
curDiskIndex = 0
with open('input.txt') as file:
    for line in file:
        for char in line.strip():
            if not space:
                for i in range(int(char)):
                    disk.append(curInputIndex)
                    curDiskIndex += 1
                space = True
                curInputIndex += 1
            else:
                for i in range(int(char)):
                    disk.append(-1)
                    curDiskIndex += 1
                space = False

ans = 0
diskLength = len(disk)
for i in range(diskLength):
    if i >= len(disk):
        break
    while disk[i] == -1:
        disk[i] = disk.pop()
    ans += disk[i] * i
print(ans)

