space = False
disk = []
curInputIndex = 0
with open('input.txt') as file:
    for line in file:
        for char in line.strip():
            if not space:
                for i in range(int(char)):
                    disk.append(curInputIndex)
                space = True
                curInputIndex += 1
            else:
                for i in range(int(char)):
                    disk.append(-1)
                space = False

endIndex = len(disk) - 1
while endIndex > 0:

    print(endIndex)

    finalElementLen = 0

    while disk[endIndex] == -1:
        endIndex -= 1
    
    number = disk[endIndex]
    for i in range(endIndex, 0, -1):
        if disk[i] == number:
            finalElementLen += 1
            endIndex -= 1
        else:
            break

    
    gapLen = 0
    for i in range(0, endIndex+1):
        if disk[i] == -1:
            gapLen += 1
            if gapLen >= finalElementLen:
                for j in range(0, finalElementLen):
                    disk[i-finalElementLen+j+1] = number
                    disk[endIndex+j+1] = -1
                break
        elif gapLen != 0:
            gapLen = 0
        


ans = 0
diskLength = len(disk)
for i in range(diskLength):
    if disk[i] != -1:
        ans += disk[i] * i
print(ans)