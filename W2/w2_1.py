count = 0
with open('input.txt') as file:
    for line in file:
        levels = map(int, line.strip().split())
        prevLevel = 10000
        valid = True
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
                        valid = False
                        break
                else:
                    if level >= prevLevel and not ascending:
                        valid = False
                        break
                    if level <= prevLevel and ascending:
                        valid = False
                        break
                if abs(level - prevLevel) > 3:
                    valid = False
                    break
                prevLevel = level
        if valid:
            #print("Safe")
            count += 1
        #else:
            #print("Unsafe")
    print(count)
                

