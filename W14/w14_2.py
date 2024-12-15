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

def getGrid(positions:list, bounds:list) -> list:
    locs = [["."] * bounds[1] for _ in range(bounds[0])]
    for position in positions:
        locs[position[0]][position[1]] = '0'
    return locs

def printRoom(positions:list, bounds:list):

    locs = getGrid(positions, bounds)
    for line in locs:
        lineStr = ''.join(map(str, line))
        print(lineStr)
    print("")


def findBiggestClusterSize(locs:list, positions:list, bounds:list):
    maxSize = 0
    for position in positions:
        if locs[position[0]][position[1]] == "0":
            size = getCluster(locs, position)
            if size > maxSize:
                maxSize = size
    return maxSize


def getCluster(locs:list, position:list):
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    count = 1
    locs[position[0]][position[1]] = '1'
    for (XDir, YDir) in dirs:
        newX = position[0] + XDir
        newY = position[1] + YDir
        if inBounds([newX, newY], bounds) and locs[newX][newY] == "0":
            tCount = getCluster(locs, [newX, newY])
            count += tCount
    return count


def inBounds(position:list, bounds:list):
    if position[0] < 0 or position[0] >= bounds[0] or position[1] < 0 or position[1] >= bounds[1]:
        return False
    return True


bounds = [101, 103]
x = 100

with open("input.txt") as file:
    positions = []
    velocities = []
    for line in file:
        posText = line.strip().split()[0]
        posStr = posText.split("=")[1].split(",")
        position = [int(posStr[0]), int(posStr[1])]
        positions.append(position)
        velocityText = line.strip().split()[1].split("=")[1]
        horVelocity = int(velocityText.split(",")[0])
        verVelocity = int(velocityText.split(",")[1])
        velocities.append([horVelocity, verVelocity])

counter = 0
while True:
    counter += 1
    for i in range(len(positions)):
        positions[i] = applyVelocity(positions[i], velocities[i][0], velocities[i][1], bounds)
    locs = getGrid(positions, bounds)
    maxCluster = findBiggestClusterSize(locs, positions, bounds)
    if(maxCluster >= 20):
        printRoom(positions, bounds)
        print("Index: " + str(counter) + "\n----\n")
