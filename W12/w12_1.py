chars = []
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def inBounds(lineIndex, colIndex):
    global chars
    if lineIndex < 0 or lineIndex >= len(chars) or colIndex < 0 or colIndex >= len(chars[0]):
        return False
    return True

def getRegion(lineIndex, colIndex, area, perimeter) -> (int, int):
    global chars, dirs
    newArea = 0
    newPerimeter = 0
    plantType = chars[lineIndex][colIndex]

    chars[lineIndex][colIndex] = chars[lineIndex][colIndex].lower()

    newArea += 1
    edgeCount = 4
    for (lineDir, colDir) in dirs:
        newLineIndex = lineIndex + lineDir
        newColIndex = colIndex + colDir
        if inBounds(newLineIndex, newColIndex):
            if chars[newLineIndex][newColIndex] == plantType or chars[newLineIndex][newColIndex] == plantType.lower():
                edgeCount -= 1

    newPerimeter += edgeCount

    for (lineDir, colDir) in dirs:
        newLineIndex = lineIndex + lineDir
        newColIndex = colIndex + colDir
        if inBounds(newLineIndex, newColIndex):
            if chars[newLineIndex][newColIndex] == plantType:
                (tArea, tPerimeter) = getRegion(newLineIndex, newColIndex, newArea, newPerimeter)
                newArea += tArea
                newPerimeter += tPerimeter

    return (newArea, newPerimeter)



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
            (area, perimeter) = getRegion(lineIndex, colIndex, 0, 0)
            #print(chars[lineIndex][colIndex].upper() + ": Area: " + str(area) + "; Perimeter: " + str(perimeter))
            price = area * perimeter
            priceSum += price
print(priceSum)

