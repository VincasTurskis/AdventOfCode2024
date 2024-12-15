def moveRobot(robotCoords: list, dirChar: list, grid: list):
    dirList = parseDir(dirChar)
    targetCoords = applyDir(robotCoords, dirList, grid)
    if getGrid(grid, targetCoords) == "#":
        return robotCoords
    if getGrid(grid, targetCoords) == '[' or getGrid(grid, targetCoords) == "]":
        if not checkIfBoxCanBeMoved(targetCoords, dirList, grid):
            return robotCoords
        moveBox(targetCoords, dirList, grid)
    targetCoords = applyDir(robotCoords, dirList, grid)
    grid[robotCoords[0]][robotCoords[1]] = '.'
    grid[targetCoords[0]][targetCoords[1]] = '@'
    return targetCoords

#returns the new coordinates of a box to move
def moveBox(coords: list, dirList: list, grid: list) -> list:
    if not checkIfBoxCanBeMoved(coords, dirList, grid):
        return coords
    # from this point on, assume its been called on the left piece
    if dirList[0] == 0:
        targetCoords = applyDir(coords, dirList, grid)
        while getGrid(grid, targetCoords) != '.':
            targetCoords = applyDir(targetCoords, dirList, grid)
            #grid[newTargetCoords[0]][newTargetCoords[1]] = getGrid(grid, targetCoords)
            #targetCoords = newTargetCoords
        reverseDir = [dirList[0], 0-dirList[1]]
        reverseTarget = applyDir(targetCoords, reverseDir, grid)
        while not compareCoords(targetCoords, coords):
            grid[targetCoords[0]][targetCoords[1]] = getGrid(grid, reverseTarget)
            targetCoords = reverseTarget
            reverseTarget = applyDir(reverseTarget, reverseDir, grid)
        grid[targetCoords[0]][targetCoords[1]] = '.'
        return applyDir(coords, dirList, grid)
    else:
        if getGrid(grid, coords) == "]":
            return moveBox([coords[0], coords[1] - 1], dirList, grid)
        targetCoordsLeft = applyDir(coords, dirList, grid)
        targetCoordsRight = [targetCoordsLeft[0], targetCoordsLeft[1] + 1]
        coordsRight = [coords[0], coords[1] + 1]
        #if getGrid(grid, targetCoordsRight) == "." and getGrid(grid, targetCoordsRight) == ".":
        if getGrid(grid, targetCoordsLeft) == "[" or getGrid(grid, targetCoordsLeft) == "]":
           moveBox(targetCoordsLeft, dirList, grid)
        #Not checking for the other bracket, that's accounted for in the previous if statement
        if getGrid(grid, targetCoordsRight) == "[":
            moveBox(targetCoordsRight, dirList, grid)
        grid[targetCoordsLeft[0]][targetCoordsLeft[1]] = "["
        grid[targetCoordsRight[0]][targetCoordsRight[1]] = "]"
        grid[coords[0]][coords[1]] = "."
        grid[coordsRight[0]][coordsRight[1]] = "."
        return targetCoordsLeft


            
def checkIfBoxCanBeMoved(coords: list, dirList: list, grid: list) -> bool:
    if getGrid(grid, coords) != "[" and getGrid(grid, coords) != "]":
        raise Exception("Not a box")
    if getGrid(grid, coords) == "]":
        return checkIfBoxCanBeMoved([coords[0], coords[1] - 1], dirList, grid)
    
    if dirList[0] == 0:
        targetCoords = applyDir(coords, dirList, grid)
        while getGrid(grid, targetCoords) != '.':
            if getGrid(grid, targetCoords) == "#":
                return False
            targetCoords = applyDir(targetCoords, dirList, grid)
        return True
    else:
        targetCoordsLeft = applyDir(coords, dirList, grid)
        targetCoordsRight = [targetCoordsLeft[0], targetCoordsLeft[1] + 1]
        if getGrid(grid, targetCoordsLeft) == "#" or getGrid(grid, targetCoordsRight) == "#":
            return False
        if getGrid(grid, targetCoordsLeft) == "[" or getGrid(grid, targetCoordsLeft) == "]":
            if not checkIfBoxCanBeMoved(targetCoordsLeft, dirList, grid):
                return False
        if getGrid(grid, targetCoordsRight) == "[":
            if not checkIfBoxCanBeMoved(targetCoordsRight, dirList, grid):
                return False
        return True
        #raise Exception("Invalid target character in checkIfBoxCanBeMoved. Chars: \'" + getGrid(grid, targetCoordsLeft) + "\', \'" + getGrid(grid, targetCoordsRight) + "\'")
def compareCoords(coords1, coords2):
    if coords1[0] == coords2[0] and coords1[1] == coords2[1]:
        return True
    return False
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
                if char == "O":
                    gridLine.append("[")
                    gridLine.append("]")
                elif char == "@":
                    currentRobotCoords = [lineIndex, colIndex]
                    gridLine.append("@")
                    gridLine.append(".")
                else:
                    gridLine.append(char)
                    gridLine.append(char)
                colIndex += 2
            grid.append(gridLine)
            lineIndex += 1
        else:
            for char in line.strip():
                currentRobotCoords = moveRobot(currentRobotCoords, char, grid)
ans = 0
for i in range(len(grid)):
    print(grid[i])
    for j in range(len(grid[i])):
        if grid[i][j] == '[':
            ans += i * 100 + j
print(ans)