wireDict = dict()

instrDict = dict()

outputDict = dict()


def operation(input1, input2, op):
    match op:
        case "AND":
            return input1 & input2
        case "OR":
            return input1 | input2
        case "XOR":
            return input1 ^ input2


def findInstruction(input1:str, input2:str, op:str) -> tuple:
    output = instrDict.get((input1, input2, op), None)
    if output != None:
        return output
    output = instrDict.get((input2, input1, op), None)
    return output

def findInputs(output:str):
    return outputDict[output]
    

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
        outputDict[result] = (inputs[0], inputs[2], inputs[1])
        curLine = file.readline().strip()

misplacedWires = []


for instruction in instrDict.keys():
    input1, input2, op = instruction
    if (input1[0] == 'x' or input1[0] == 'y') and (input2[0] == 'x' or input2[0] == 'y') and (op == "XOR" or op == "AND") and (instrDict[instruction][0] != 'z'):
        continue
    if (input1[0] != 'x' and input1[0] != 'y') and (input2[0] != 'x' and input2[0] != 'y') and (op == "XOR") and (instrDict[instruction][0] == 'z'):
        continue
    if (input1[0] != 'x' and input1[0] != 'y') and (input2[0] != 'x' and input2[0] != 'y') and (op == "OR" or op == "AND") and (instrDict[instruction][0] != 'z'):
        continue
    misplacedWires.append(instrDict[instruction])

print(','.join(sorted(misplacedWires)))
misplacedWires = []

def findCorrectValue(rightInput, rightOutput):
    reverseInput1, reverseInput2, _ = outputDict[rightOutput]
    if rightInput == reverseInput1:
        return reverseInput2
    elif rightInput == reverseInput2:
        return reverseInput1
    else:
        raise Exception("Neither input is right")

def findInstructionWith1Input(input, op):
    for instruction in instrDict:
        input1, input2, curOp = instruction
        if op == curOp:
            if input1 == input or input2 == input:
                return instruction
    return None


carryIn = findInstruction("x00", "y00", "AND")
for i in range(1, 45):
    input1 = "x" + str(i).zfill(2)
    input2 = "y" + str(i).zfill(2)
    output = "z" + str(i).zfill(2)

    wire2 = findInstruction(input1, input2, "XOR")

    reverseInputs = findInputs(output)

    if wire2 not in reverseInputs:
        if carryIn not in reverseInputs:
            misplacedWires.append(output)
        else:
            misplacedWires.append(wire2)
            wire2 = findCorrectValue(carryIn, output)
    elif carryIn not in reverseInputs:
        misplacedWires.append(carryIn)
        carryIn = findCorrectValue(wire2, output)

    

    

    wire3 = findInstruction(wire2, carryIn, "AND")
    if wire3 == None:
        raise Exception("Wire 3 should be correct at this point")

    wire4 = findInstruction(input1, input2, "AND")

    carryOut = findInstruction(wire4, wire3, "OR")
    if carryOut == None:
        wire4Search = findInstructionWith1Input(wire4, "OR")
        wire3Search = findInstructionWith1Input(wire3, "OR")
        if wire4Search == None:
            misplacedWires.append(wire4)
            wire4 = findCorrectValue(wire3, instrDict[wire3Search])
        elif wire3Search == None:
            misplacedWires.append(wire3)
            wire4 = findCorrectValue(wire4, instrDict[wire4Search])
        else:
            raise Exception("Fuck")
        carryOut = findInstruction(wire4, wire3, "OR")

    carryIn = carryOut

print(misplacedWires)