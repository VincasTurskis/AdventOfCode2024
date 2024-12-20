import heapq

GRID_SIZE_X = 0
GRID_SIZE_Y = 0
START_COORDS = tuple()
END_COORDS = tuple()
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
grid = []

def canBeSkipped(coords:tuple, grid:list) -> bool:
    x, y = coords
    if grid[x][y] != "#":
        return False
    if inBounds((x-1, y)) and inBounds((x+1, y)):
        if grid[x-1][y] == '.' and grid[x+1][y] == '.':
            return True
    if inBounds((x, y-1)) and inBounds((x, y+1)):
        if grid[x][y-1] == '.' and grid[x][y+1] == '.':
            return True
    return False

def heuristic(coords:tuple, goal:tuple):
    sX, sY = coords
    gX, gY = goal
    return(abs(sX - gX) + abs(sY - gY))

def buildPath(cameFrom:dict, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

def inBounds(coords):
    x, y = coords
    if x < 0 or x >= GRID_SIZE_X or y < 0 or y >= GRID_SIZE_Y:
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
            if grid[newLine][newCol] != "#":
                neighbors.append((newLine, newCol))
    return neighbors

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

with open("input.txt") as file:
    i = 0
    for line in file:
        gridLine = []
        for j in range(len(line.strip())):
            if line[j] == 'S':
                START_COORDS = (i, j)
                gridLine.append('.')
            elif line[j] == 'E':
                END_COORDS = (i, j)
                gridLine.append('.')
            else:
                gridLine.append(line[j])
        grid.append(gridLine)
        GRID_SIZE_Y = len(gridLine)
        i += 1
GRID_SIZE_X = len(grid)

init_path = AStar(grid, START_COORDS, END_COORDS)
init_count = len(init_path)

ans = 0
counter = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        counter += 1
        if counter % 100 == 0:
            print(counter)
        if canBeSkipped((i, j), grid):
            grid[i][j] = '.'
            new_path = AStar(grid, START_COORDS, END_COORDS)
            new_count = len(new_path)
            if init_count - new_count >= 100:
                ans += 1
            grid[i][j] = "#"

print(ans)
