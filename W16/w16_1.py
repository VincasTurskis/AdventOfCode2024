import heapq

graph = dict()
startCoords = ()
startDir = (0, 1)
endCoords = ()
maze = []
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def DijkstrasAlg(graph, startCoords):
    pq = []
    heapq.heappush(pq, (0, startCoords))
    distances = {node: float('inf') for node in graph}
    distances[startCoords] = 0
    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Skip if we've already found a better way
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            # Only consider this path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def GetNeighbors(key, maze):
    neighbors = []
    coords, dir = key
    x, y = coords
    dirX, dirY = dir
    if maze[x+dirX][y+dirY] != '#':
        neighbors.append((((x+dirX, y+dirY), dir), 1))
    for dirNeighbor in GetDirNeighbors(dir):
        neighbors.append(((coords, dirNeighbor), 1000))
    return neighbors


def GetDirNeighbors(dir: tuple):
    dirX, dirY = dir
    if dirX != 0:
        dir1 = (0, 1)
        dir2 = (0, -1)
    else:
        dir1 = (1, 0)
        dir2 = (-1, 0)
    return [dir1, dir2]

def ReverseDir(dir):
    dirX, dirY = dir
    return (0-dirX, 0-dirY)

with open("input.txt") as file:
    for line in file:
        maze.append(list(line.strip()))

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == '#':
            continue
        for dir in dirs:
            key = ((i, j), dir)
            graph[key] = GetNeighbors(key, maze)
            match maze[i][j]:
                case '.':
                    pass
                case 'S':
                    startCoords = ((i, j), startDir)
                case 'E':
                    endCoords = (i, j)

forwardDistances = DijkstrasAlg(graph, startCoords)
for dir in dirs:
    print(forwardDistances[(endCoords, dir)])    

