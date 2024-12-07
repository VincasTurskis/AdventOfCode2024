#y = [row[:] for row in x]


baseGrid = []
originalWalkGrid = []
workingGrid = []
curLine = 0
def inBounds(pos: tuple) -> bool:
    (line, col) = pos
    if col < 0 or col >= len(baseGrid) or line < 0 or line >= len(baseGrid[0]):
        return False
    return True

counter = 0
stepCounter = 0
guardDir = (-1, 0)
guardPos = (0, 0)
ogGuardPos = (0, 0)
loop = False


def getMoveDest(curPos, curDir):
    (curLine, curCol) = curPos
    (dirLine, dirCol) = curDir
    curLine += dirLine
    curCol += dirCol
    ans = (curLine, curCol)
    return ans



with open('input.txt') as file:
    for line in file:
        curCol = 0
        lineChars = list(line)
        lineArr = []
        for char in lineChars:
            if char == ".":
                lineArr.append(0)
            if char == "#":
                lineArr.append(-1)
            if char == "^":
                lineArr.append(1)
                guardPos = (curLine, curCol)
                ogGuardPos = (curLine, curCol)
            curCol += 1
        baseGrid.append(lineArr)
        curLine += 1
workingGrid = [row[:] for row in baseGrid]

def reset():
    global guardPos, guardDir, ogGuardPos, workingGrid, baseGrid, loop, stepCounter
    (i, j) = ogGuardPos
    guardPos = (i, j)
    guardDir = (-1, 0)
    workingGrid = [row[:] for row in baseGrid]
    loop = False
    stepCounter = 0


def dirToInt(dir: tuple):
    (line, col) = dir
    ans = -1
    if line == -1 and col == 0:
        ans = 1
    if line == 0 and col == 1:
        ans = 2
    if line == 1 and col == 0:
        ans = 3
    if line == 0 and col == -1:
        ans = 4
    return ans 

def move():
    global guardPos, guardDir
    #if inBounds(getMoveDest(guardPos, guardDir)):
    (curLine, curCol) = guardPos
    workingGrid[curLine][curCol] = dirToInt(guardDir)
    guardPos = getMoveDest(guardPos, guardDir)

def turnRight():
    global guardDir, guardPos, loop
    (line, col) = guardDir


    if line != 0:
        col = 0 - line
        line = 0
    else:
        line = col
        col = 0

    
    (curLine, curCol) = guardPos
    guardDir = (line, col)
    if workingGrid[curLine][curCol] == dirToInt(guardDir):
        loop = True
    else:
        workingGrid[curLine][curCol] = dirToInt(guardDir)


while inBounds(guardPos):
    target = getMoveDest(guardPos, guardDir)
    if inBounds(target):
        (targetLine, targetCol) = target
        if workingGrid[targetLine][targetCol] >= 0:
            move()
        elif workingGrid[targetLine][targetCol] == -1:
            turnRight()
        else:
            print("Heck")
            break
    else:
        move()


originalWalkGrid = [row[:] for row in workingGrid]
reset()
for i in range(len(originalWalkGrid)):
    print(i)
    if(i == 5):
        pass
        #print("")
    for j in range(len(originalWalkGrid[i])):
        if originalWalkGrid[i][j] > 0:
            if i == 5:
                pass
            reset()
            workingGrid[i][j] = -1
            while inBounds(guardPos) and not loop and stepCounter < 100000:
                target = getMoveDest(guardPos, guardDir)
                if inBounds(target):
                    (targetLine, targetCol) = target
                    if workingGrid[targetLine][targetCol] >= 0:
                        move()
                    elif workingGrid[targetLine][targetCol] == -1:
                        turnRight()
                    else:
                        print("Heck")
                        break
                else:
                    move()
                stepCounter += 1
            if loop or stepCounter >=100000:
                #print("loop here")
                counter += 1
print(" ")
print(counter)