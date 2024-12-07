from collections import deque

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

def relevantRules(order):
    relRules = []
    for rule in rules:
        first, second = rule
        if first in order and second in order:
            relRules.append(rule)
    return relRules

def kahnAlg(vertices, nodes):
    inDegree = dict()
    q = deque()
    result = []
    graphDict = dict()
    for node in nodes:
        inDegree[node] = 0
        graphDict[node] = []
    for (start, end) in vertices:
        inDegree[end] += 1
        graphDict[start].append(end)
    for node in nodes:
        if inDegree[node] == 0:
            q.append(node)

    while q:
        nodeToAppend = q.popleft()
        result.append(nodeToAppend)
        for node in graphDict[nodeToAppend]:
            inDegree[node] -= 1
            if inDegree[node] == 0:
                q.append(node)
    return result

for order in orders:
    orderWrong = False
    relRules = []
    for rule in rules:
        if not followsRule(order, rule):
            orderWrong = True
            relRules = relevantRules(order)
            break
    if orderWrong:
        sortedOrder = kahnAlg(relRules, order)
        middleSum += sortedOrder[int(len(sortedOrder)/2)] 
print(middleSum)