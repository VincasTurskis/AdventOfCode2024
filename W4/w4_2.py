charMatrix = []

def increment(num: int) -> int:
    if num < 0:
        return num - 1
    if num > 0:
        return num + 1
    return num
def inBounds(x, y) -> bool:
    if x < 0 or x >= len(charMatrix):
        return False
    if y < 0 or y >= len(charMatrix):
        return False
    return True

def checkIfXmas(i: int, j: int) -> bool:

    if not inBounds(i-1, j-1) or not inBounds(i+1, j-1) or not inBounds(i-1, j+1) or not inBounds(i+1, j+1):
        return False

    if (charMatrix[i-1][j+1] == 'M' and charMatrix[i+1][j-1] == 'S') or (charMatrix[i-1][j+1] == 'S' and charMatrix[i+1][j-1] == 'M'):
        if (charMatrix[i+1][j+1] == 'M' and charMatrix[i-1][j-1] == 'S') or (charMatrix[i+1][j+1] == 'S' and charMatrix[i-1][j-1] == 'M'):
            return True
    return False

with open('input.txt') as file:
    for line in file:
        charMatrix.append(list(line.strip()))

sum = 0
for i in range(0, len(charMatrix)):
    for j in range(0, len(charMatrix)):
        if charMatrix[i][j] == 'A':
            if checkIfXmas(i, j):
                sum += 1

print(sum)