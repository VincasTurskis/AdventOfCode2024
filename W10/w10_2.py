topoMap = []

def inBounds(lineIndex, colIndex, topoMap):
    if lineIndex < 0 or lineIndex >= len(topoMap) or colIndex < 0 or colIndex >= len(topoMap[0]):
        return False
    return True

def findTrailScore(lineIndex: int, colIndex: int, topoMap: list) -> int:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    trails = 0
    for direction in directions:
        newLineIndex = lineIndex + direction[0]
        newColIndex = colIndex + direction[1]
        if inBounds(newLineIndex, newColIndex, topoMap):
            if topoMap[newLineIndex][newColIndex] - topoMap[lineIndex][colIndex] == 1:
                trails += trailStep(newLineIndex, newColIndex, topoMap, trails)
    return trails

    

def trailStep(lineIndex: int, colIndex: int, topoMap: list, trails: int):
    if topoMap[lineIndex][colIndex] == 9:
        return 1
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    trailCount = 0
    for direction in directions:
        newLineIndex = lineIndex + direction[0]
        newColIndex = colIndex + direction[1]
        if inBounds(newLineIndex, newColIndex, topoMap):
            if topoMap[newLineIndex][newColIndex] - topoMap[lineIndex][colIndex] == 1:
                trailCount += trailStep(newLineIndex, newColIndex, topoMap, trails)
    return trailCount

with open("input.txt") as file:
    for line in file:
        mapLine = []
        for char in line.strip():
            mapLine.append(int(char))
        topoMap.append(mapLine)

ans = 0
for lineIndex in range(len(topoMap)):
    for colIndex in range(len(topoMap[lineIndex])):
        if topoMap[lineIndex][colIndex] == 0:
            ans += findTrailScore(lineIndex, colIndex, topoMap)
print(ans)
