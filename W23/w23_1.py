
computer_dict = dict()
connections = set()


lan_sets = set()

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
    if len(computer_dict[computer]) < 2:
        continue
    for connection1 in computer_dict[computer]:
        for connection2 in computer_dict[computer]:
            if isConnected(connection1, connection2):
                lan_sets.add(tuple(sorted((computer, connection1, connection2))))

sum = 0
for entry in lan_sets:
    a, b, c = entry
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        sum += 1
        continue
print(sum)
