def applyRules(pattern: str, rules: list):
    for rule in rules:
        if pattern[0:len(rule)] == rule:
            rem = pattern[len(rule):]
            if rem == "":
                return True
            if applyRules(rem, rules):
                return True
    return False

with open("input.txt") as file:
    towels = file.readline().strip().split(", ")
    file.readline()
    pattern = file.readline().strip()
    counter = 0
    while pattern != "":
        if applyRules(pattern, towels):
            counter += 1
        pattern = file.readline().strip()
    print(counter)  