import math

antennaDict = dict()

def inBounds(loc:list, maxLineIndex:int, maxColIndex:int) -> bool:
    if loc[0] < 0 or loc[0] >= maxLineIndex or loc[1] < 0 or loc[1] >= maxColIndex:
        return False
    return True

def addCoords(coord1, coord2):
    return [coord1[0]+coord2[0], coord1[1]+coord2[1]]
def subtractCoords(coord1, coord2):
    return [coord1[0]-coord2[0], coord1[1]-coord2[1]]

antinodeLocs = set()
maxLineIndex = 0
maxColIndex = 0


def getAntinodeLocsFromFrequency(frequencyLocs: list):
    global antinodeLocs
    global maxLineIndex, maxColIndex
    for i in range(0, len(frequencyLocs)-1):
        for j in range(i+1, len(frequencyLocs)):
            locDiff = [0, 0]
            locDiff[0] = frequencyLocs[j][0] - frequencyLocs[i][0]
            locDiff[1] = frequencyLocs[j][1] - frequencyLocs[i][1]
            interval=[int(locDiff[0]/math.gcd(locDiff[0], locDiff[1])), int(locDiff[1]/math.gcd(locDiff[0], locDiff[1]))]
            curLoc = frequencyLocs[i]
            while inBounds(curLoc, maxLineIndex, maxColIndex):
                antinodeLocs.add(str(curLoc))
                curLoc = addCoords(curLoc, interval)
            curLoc = frequencyLocs[i]
            while inBounds(curLoc, maxLineIndex, maxColIndex):
                antinodeLocs.add(str(curLoc))
                curLoc = subtractCoords(curLoc, interval)


with open("input.txt") as file:
    lineIndex = 0
    for line in file:
        colIndex = 0
        for char in line.strip():
            if char != ".":
                if char in antennaDict:
                    antennaDict[char].append([lineIndex, colIndex])
                else:
                    antennaDict[char] = [[lineIndex, colIndex]]
            colIndex += 1
        maxColIndex = colIndex
        lineIndex += 1
    maxLineIndex = lineIndex

    for key in antennaDict:
        getAntinodeLocsFromFrequency(antennaDict[key])

    print(len(antinodeLocs))