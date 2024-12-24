wireDict = dict()

instrDict = dict()


def operation(input1, input2, op):
    match op:
        case "AND":
            return input1 & input2
        case "OR":
            return input1 | input2
        case "XOR":
            return input1 ^ input2

with open("input.txt") as file:
    curLine = file.readline().strip()
    while curLine != "":
        wireDict[curLine.split(": ")[0]] = int(curLine.split(": ")[1])
        curLine = file.readline().strip()
    curLine = file.readline().strip()
    while curLine != "":
        splitLine = curLine.split(" -> ")
        result = splitLine[1]
        inputs = splitLine[0].split()
        instrDict[(inputs[0], inputs[2], inputs[1])] = result
        curLine = file.readline().strip()

counter = 0
while instrDict:
    counter += 1
    if counter % 100 == 0:
        print(counter)
    instrToPop = None
    for instruction in instrDict.keys():
        input1, input2, op = instruction
        if input1 in wireDict.keys() and input2 in wireDict.keys():
            wireDict[instrDict[instruction]] = operation(wireDict[input1], wireDict[input2], op)
            instrToPop = instruction
            break
    if instrToPop == None:
        raise Exception("No next instruction found")
    instrDict.pop(instruction)

binaryAns = [-1] * 46

for wire in wireDict.keys():
    if wire[0] == 'z':
        num = int(wire[1:3])
        binaryAns[-(num + 1)] = wireDict[wire]

binaryStr = "".join(map(str, binaryAns))
print(int(binaryStr, 2))

