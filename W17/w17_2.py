with open("input.txt") as file:
    A = int(file.readline().strip().split(": ")[1])
    B = int(file.readline().strip().split(": ")[1])
    B = int(file.readline().strip().split(": ")[1])
    file.readline()
    program = file.readline().strip().split(": ")[1].split(",")

def AToOutput(AVal:int):
    BVal = 0
    CVal = 0
    BVal = (AVal % 8) ^ 2
    CVal = AVal // (2**BVal)
    BVal = (BVal^CVal)^7
    return BVal % 8

curAVal = 0

def findAVal(curAVal:int, index:int):
    global program
    if index < 0:
        return curAVal // 8
    target = int(program[index])
    for i in range(8):
        curOutput = AToOutput(curAVal + i)
        if curOutput == target:
            result = findAVal((curAVal + i) * 8, index - 1)
            if result is not None:
                return result
    return None

print(findAVal(0, len(program) - 1))