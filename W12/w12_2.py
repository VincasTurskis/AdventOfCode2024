chars = []
sideDict = dict()
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def inBounds(lineIndex, colIndex):
    global chars
    if lineIndex < 0 or lineIndex >= len(chars) or colIndex < 0 or colIndex >= len(chars[0]):
        return False
    return True

def countEdges(numberList):
    if not numberList:
        return 0
    numbers = sorted(numberList)

    count = 1  # Start with the first set

    for i in range(1, len(numbers)):
        # Check if the current number is not consecutive to the previous
        if numbers[i] != numbers[i - 1] + 1:
            count += 1
    return count

def getRegion(lineIndex, colIndex, area) -> (int, int):
    global chars, dirs, sideDict
    newArea = 0
    plantType = chars[lineIndex][colIndex]

    chars[lineIndex][colIndex] = chars[lineIndex][colIndex].lower()

    newArea += 1
    edgeCount = 4
    for (lineDir, colDir) in dirs:
        newLineIndex = lineIndex + lineDir
        newColIndex = colIndex + colDir
        if inBounds(newLineIndex, newColIndex) and (chars[newLineIndex][newColIndex] == plantType or chars[newLineIndex][newColIndex] == plantType.lower()):
            pass
        else:
            key = ""
            if colDir==0:
                key = "hor"+str(lineIndex)+"dir"+str(lineDir)
                if key not in sideDict:
                    sideDict[key]=[]
                sideDict[key].append(colIndex)
            else:
                key = "ver"+str(colIndex)+"dir"+str(colDir)
                if key not in sideDict:
                    sideDict[key]=[]
                sideDict[key].append(lineIndex)

    for (lineDir, colDir) in dirs:
        newLineIndex = lineIndex + lineDir
        newColIndex = colIndex + colDir
        if inBounds(newLineIndex, newColIndex):
            if chars[newLineIndex][newColIndex] == plantType:
                tArea = getRegion(newLineIndex, newColIndex, newArea)
                newArea += tArea

    return newArea



with open("input.txt") as file:
    for line in file:
        charLine = []
        for char in line.strip():
            charLine.append(char)
        chars.append(charLine)

priceSum = 0
for lineIndex in range(len(chars)):
    for colIndex in range(len(chars[lineIndex])):
        if chars[lineIndex][colIndex].isupper():
            sideDict = dict()
            area = getRegion(lineIndex, colIndex, 0)
            sideCount = 0
            for key in sideDict:
                sideCount += countEdges(sideDict[key])
            price = area * sideCount
            priceSum += price
print(priceSum)

