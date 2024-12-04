def isSafe(levels: list) -> bool:
    prevLevel = 10000
    ascending = None
    for level in levels:
        if prevLevel == 10000:
            prevLevel = level
        else:
            if ascending == None:
                if level > prevLevel:
                    ascending = True
                elif level < prevLevel:
                    ascending = False
                else:
                    return False
            else:
                if level >= prevLevel and not ascending:
                    return False
                if level <= prevLevel and ascending:
                    return False
            if abs(level - prevLevel) > 3:
                return False
            prevLevel = level
    return True

def canBeFixed(levels):
    for i in range(len(levels)):
        elem = levels[i]
        del levels[i]
        if isSafe(levels):
            return True
        levels.insert(i, elem)
    return False


count = 0

with open('input.txt') as file:
    for line in file:
        levels = list(map(int, line.strip().split()))
        if isSafe(levels):
            count += 1
        elif canBeFixed(levels):
            count += 1
    
    print(count)


