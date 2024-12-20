import functools

rules = []
patternDict = dict()

#@functools.cache
def applyRules(pattern: str):
    if pattern in patternDict:
        return patternDict[pattern]
    global rules
    counter = 0
    if pattern == "":
        return 1
    for rule in rules:
        if pattern[0:len(rule)] == rule:
            rem = pattern[len(rule):]
            counter += applyRules(rem)
    patternDict[pattern] = counter
    return counter

with open("input.txt") as file:
    rules = file.readline().strip().split(", ")
    file.readline()
    pattern = file.readline().strip()
    counter = 0
    while pattern != "":
        counter += applyRules(pattern)
        pattern = file.readline().strip()
    print(counter)  