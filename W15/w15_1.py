def moveRobot(robotCoords: list, dirChar: list, grid: list):
    dirList = parseDir(dirChar)
    targetCoords = applyDir(robotCoords, dirList, grid)
    while inBounds(targetCoords, grid):
        if getGrid(grid, targetCoords) == "#":
            return robotCoords
        if getGrid(grid, targetCoords) == ".":
            break
        targetCoords = applyDir(targetCoords, dirList, grid)
    targetCoords = applyDir(robotCoords, dirList, grid)
    grid[robotCoords[0]][robotCoords[1]] = "."
    if grid[targetCoords[0]][targetCoords[1]] == 'O':
        
        targetCoords = applyDir(targetCoords, dirList, grid)
        while getGrid(grid, targetCoords) == 'O':
            targetCoords = applyDir(targetCoords, dirList, grid)
        grid[targetCoords[0]][targetCoords[1]] = 'O'
        targetCoords = applyDir(robotCoords, dirList, grid)
    grid[targetCoords[0]][targetCoords[1]] = '@'
    return targetCoords



def inBounds(coords: list, grid: list) -> bool:
    if coords[0] < 0 or coords[0] >= len(grid) or coords[1] < 0 or coords[1] >= len(grid[0]):
        return False
    return True

def parseDir(dirChar: str) -> list:
    match dirChar:
        case '^':
            return [-1, 0]
        case 'v':
            return [1, 0]
        case '>':
            return [0, 1]
        case '<':
            return [0, -1]
        case _:
            raise Exception("unparsable direction in parseDir")

def applyDir(coords: list, dirList: list, grid: list):
    newCoords = [coords[0]+dirList[0], coords[1]+dirList[1]]
    return newCoords

grid = []

def getGrid(grid: list, coords: list) -> list:
    return grid[coords[0]][coords[1]]

currentRobotCoords = []
with open("input.txt") as file:
    readGrid = True
    lineIndex = 0
    for line in file:
        colIndex = 0
        if line.strip() == "":
            readGrid = False
        elif readGrid:
            gridLine = []
            for char in line.strip():
                gridLine.append(char)
                if char == "@":
                    currentRobotCoords = [lineIndex, colIndex]
                colIndex += 1
            grid.append(gridLine)
            lineIndex += 1
        else:
            for char in line.strip():
                currentRobotCoords = moveRobot(currentRobotCoords, char, grid)
ans = 0
for i in range(len(grid)):
    print(grid[i])
    for j in range(len(grid[i])):
        if grid[i][j] == 'O':
            ans += i * 100 + j
print(ans)