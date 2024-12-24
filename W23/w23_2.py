
computer_dict = dict()
connections = set()

lan_sets = set()

groups = []

def isConnected(computer1, computer2):
    str1 = computer1 + "-" + computer2
    str2 = computer2 + "-" + computer1
    if str1 in connections or str2 in connections:
        return True
    return False

with open("input.txt") as file:
    for line in file:
        computers = line.strip().split("-")
        temp = computer_dict.get(computers[0])
        if temp == None:
            temp = []
        temp.append(computers[1])
        computer_dict[computers[0]] = temp
        temp = computer_dict.get(computers[1])
        if temp == None:
            temp = []
        temp.append(computers[0])
        computer_dict[computers[1]] = temp
        connections.add(line.strip())

for computer in computer_dict.keys():
    for group in groups:
        connected = True
        for item in group:
            if not isConnected(computer, item):
                connected = False
                break
        if connected:
            groups.append(group + [computer])
    groups.append([computer])

maxLen = 0
maxGroup = []
for group in groups:
    if len(group) > maxLen:
        maxLen = len(group)
        maxGroup = ','.join(sorted(group))

print(maxGroup)

