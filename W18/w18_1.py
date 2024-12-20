import heapq
import numpy

GRID_SIZE = 71
START_COORDS = (0, 0)
END_COORDS = (70, 70)
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def heuristic(coords:tuple, goal:tuple):
    sX, sY = coords
    gX, gY = goal
    return(abs(sX - gX) + abs(sY - gY))

def setObstacle(grid, coords:tuple):
    x, y = coords
    grid[x][y] = 1


def inBounds(coords):
    x, y = coords
    if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
        return False
    return True

def getNeighbors(grid, coords):
    line, col = coords
    neighbors = []
    for dir in DIRS:
        dirLine, dirCol = dir
        newLine = line + dirLine
        newCol = col + dirCol
        if inBounds((newLine, newCol)):
            if grid[newLine][newCol] != 1:
                neighbors.append((newLine, newCol))
    return neighbors

def buildPath(cameFrom:dict, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

def AStar(grid, start_coords, end_coords):
    knownScore = dict()
    knownScore[start_coords] = 0

    heurScore = dict()
    heurScore[start_coords] = heuristic(start_coords, end_coords)

    openSet = []
    heapq.heappush(openSet, (heurScore[start_coords], start_coords))

    cameFrom = dict()

    while openSet:
        _, current = heapq.heappop(openSet)
        if current == end_coords:
            return buildPath(cameFrom, current)
        for neighbor in getNeighbors(grid, current):
            possible_score = knownScore[current] + 1
            if possible_score < knownScore.get(neighbor, float('inf')):
                cameFrom[neighbor] = current
                knownScore[neighbor] = possible_score
                heurScore[neighbor] = possible_score + heuristic(neighbor, end_coords)
                if neighbor not in openSet:
                    heapq.heappush(openSet, (heurScore[neighbor], neighbor))
    
    raise Exception("No path")


grid = [ [0]*GRID_SIZE for _ in range(GRID_SIZE) ]
with open("input.txt") as file:
    counter = 0
    for line in file:
        if counter >= 1024:
            break
        coords = line.strip().split(",")
        setObstacle(grid, (int(coords[0]), int(coords[1])))
        counter += 1
    path = AStar(grid, START_COORDS, END_COORDS)
    print(len(path) - 1)