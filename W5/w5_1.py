
readingRules = True
rules = []
orders = []
with open('input.txt') as file:
    for line in file:
        if line.strip() == "":
            readingRules = False
        elif readingRules:
            rule = line.strip().split("|")
            rules.append((int(rule[0]), int(rule[1])))
        else:
            order = line.strip().split(",")
            orders.append(list(map(int, order)))

middleSum = 0

def followsRule(order, rule) -> bool:
    first, second = rule
    if first not in order or second not in order:
        return True
    for item in order:
        if item == first:
            return True
        if item == second:
            return False
for order in orders:
    orderWrong = False
    for rule in rules:
        if not followsRule(order, rule):
            orderWrong = True
            break
    if orderWrong:
        continue
    middleSum += order[int(len(order)/2)]
print(middleSum)