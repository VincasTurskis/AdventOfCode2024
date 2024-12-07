#y = [row[:] for row in x]


grid = []
curLine = 0
def inBounds(pos: tuple) -> bool:
    (line, col) = pos
    if col < 0 or col >= len(grid) or line < 0 or line >= len(grid[0]):
        return False
    return True

counter = 0
guardDir = (-1, 0)
guardPos = (0, 0)



def getMoveDest(curPos, curDir):
    (curLine, curCol) = curPos
    (dirLine, dirCol) = curDir
    curLine += dirLine
    curCol += dirCol
    ans = (curLine, curCol)
    return ans



with open('inputTest.txt') as file:
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
                counter += 1
            curCol += 1
        grid.append(lineArr)
        curLine += 1

def move():
    global guardPos, guardDir, counter
    guardPos = getMoveDest(guardPos, guardDir)
    if inBounds(guardPos):
        (curLine, curCol) = guardPos
        if grid[curLine][curCol] == 0:
            counter += 1
        grid[curLine][curCol] += 1

def turnRight():
    global guardDir
    (line, col) = guardDir
    if line != 0:
        col = 0 - line
        line = 0
    else:
        line = col
        col = 0
    guardDir = (line, col)


while inBounds(guardPos):
    if counter % 1000 == 0:
        print("counter: " + str(counter))
    target = getMoveDest(guardPos, guardDir)
    if inBounds(target):
        (targetLine, targetCol) = target
        if grid[targetLine][targetCol] >= 0:
            move()
        elif grid[targetLine][targetCol] == -1:
            turnRight()
        else:
            print("Heck")
            break
    else:
        break
print(counter)