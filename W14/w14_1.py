def applyVelocity(position:list, horVelocity:int, verVelocity:int, bounds:list):
    newPosition = [position[0], position[1]]
    newPosition[0] = newPosition[0] + horVelocity
    if newPosition[0] < 0:
        newPosition[0] = bounds[0] + newPosition[0]
    elif newPosition[0] >= bounds[0]:
        newPosition[0] = newPosition[0] - bounds[0]

    newPosition[1] = newPosition[1] + verVelocity
    if newPosition[1] < 0:
        newPosition[1] = bounds[1] + newPosition[1]
    elif newPosition[1] >= bounds[1]:
        newPosition[1] = newPosition[1] - bounds[1]
    return newPosition
    


def findLocationAfterXMoves(x:int, position:list, horVelocity:int, verVelocity:int, bounds:list) -> list:
    pos = [position[0], position[1]]
    for i in range(x):
        pos = applyVelocity(pos, horVelocity, verVelocity, bounds)
    return pos

def findQuadrant(position:list, bounds:list) -> int:
    middleX = bounds[0] // 2
    middleY = bounds[1] // 2
    if position[0] == middleX or position[1] == middleY:
        return 4
    if position[0] < middleX:
        if position[1] < middleY:
            return 0
        return 1
    else:
        if position[1] < middleY:
            return 2
        return 3

bounds = [101, 103]
x = 100

with open("input.txt") as file:
    quadrants = [0, 0, 0, 0, 0]
    for line in file:
        posText = line.strip().split()[0]
        posStr = posText.split("=")[1].split(",")
        position = [int(posStr[0]), int(posStr[1])]
        velocityText = line.strip().split()[1].split("=")[1]
        horVelocity = int(velocityText.split(",")[0])
        verVelocity = int(velocityText.split(",")[1])
        newPosition = findLocationAfterXMoves(x, position, horVelocity, verVelocity, bounds)
        quadrants[findQuadrant(newPosition, bounds)] += 1
        print(newPosition)

ans = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print(quadrants)
print(ans)
