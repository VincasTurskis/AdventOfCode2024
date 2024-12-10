topoMap = []

def inBounds(lineIndex, colIndex, topoMap):
    if lineIndex < 0 or lineIndex >= len(topoMap) or colIndex < 0 or colIndex >= len(topoMap[0]):
        return False
    return True

def findTrailScore(lineIndex: int, colIndex: int, topoMap: list) -> int:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    trailEnds = set()
    for direction in directions:
        newLineIndex = lineIndex + direction[0]
        newColIndex = colIndex + direction[1]
        if inBounds(newLineIndex, newColIndex, topoMap):
            if topoMap[newLineIndex][newColIndex] - topoMap[lineIndex][colIndex] == 1:
                trailStep(newLineIndex, newColIndex, topoMap, trailEnds)
    return len(trailEnds)

    

def trailStep(lineIndex: int, colIndex: int, topoMap: list, trailEnds: set):
    if topoMap[lineIndex][colIndex] == 9:
        loc = [lineIndex, colIndex]
        trailEnds.add(str(loc))
        return
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for direction in directions:
        newLineIndex = lineIndex + direction[0]
        newColIndex = colIndex + direction[1]
        if inBounds(newLineIndex, newColIndex, topoMap):
            if topoMap[newLineIndex][newColIndex] - topoMap[lineIndex][colIndex] == 1:
                trailStep(newLineIndex, newColIndex, topoMap, trailEnds)

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
