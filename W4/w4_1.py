charMatrix = []

def increment(num: int) -> int:
    if num < 0:
        return num - 1
    if num > 0:
        return num + 1
    return num
def inBounds(x, y) -> str:
    if x < 0 or x >= len(charMatrix):
        return 'NO'
    if y < 0 or y >= len(charMatrix):
        return 'NO'
    return charMatrix[x][y]

def countXmasforX(i: int, j: int) -> int:
    numOfXmas = 0
    for xAxis in range(-1, 2):
        for yAxis in range(-1, 2):
            if inBounds(i + xAxis, j + yAxis) == 'M':
                xVector = increment(xAxis)
                yVector = increment(yAxis)
                if inBounds(i + xVector, j + yVector) == 'A':
                    xVector = increment(xVector)
                    yVector = increment(yVector)
                    if inBounds(i + xVector, j + yVector) == 'S':
                        numOfXmas += 1
    return numOfXmas

with open('input.txt') as file:
    for line in file:
        charMatrix.append(list(line.strip()))

sum = 0
for i in range(0, len(charMatrix)):
    for j in range(0, len(charMatrix)):
        if charMatrix[i][j] == 'X':
            sum += countXmasforX(i, j)

print(sum)

