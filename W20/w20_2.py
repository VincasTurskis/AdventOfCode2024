import heapq

GRID_SIZE_X = 0
GRID_SIZE_Y = 0
START_COORDS = tuple()
END_COORDS = tuple()
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
CHEAT_LIMIT = 20
CHEAT_INCREASE_THRESHOLD = 100
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

def buildPath(cameFrom:dict, current) -> dict:
    total_path = dict()
    total_path[current] = 0
    length = 0
    while current in cameFrom.keys():
        length += 1
        current = cameFrom[current]
        total_path[current] = length
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

def getCheatDestinations(coords: tuple, grid: list, cheat_limit: int) -> list:
    dests = []
    x, y = coords
    for i in range(0-cheat_limit, cheat_limit+1):
        for j in range(0-(cheat_limit-abs(i)), cheat_limit-abs(i)+1):
            if inBounds((x+i, y+j)):
                if grid[x+i][y+j] == '.':
                    dests.append((x+i, y+j))
    return dests




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

ans = 0
init_path = AStar(grid, START_COORDS, END_COORDS)

for coords in init_path.keys():
    dests = getCheatDestinations(coords, grid, CHEAT_LIMIT)
    for dest in dests:
        cheat_start_dist = init_path[coords]
        cheat_end_dist = init_path[dest]
        total_saved_time = init_path[coords] - init_path[dest]
        cX, cY = coords
        dX, dY = dest
        cheat_duration = abs(cX - dX) + abs(cY- dY)
        if total_saved_time - cheat_duration >= CHEAT_INCREASE_THRESHOLD:
            ans += 1

print(ans)
