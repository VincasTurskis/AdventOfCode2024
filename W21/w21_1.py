#Every button can be navigated to with 2 buttons from the dir pad in the level above, followed by a press of A.

NUM_PAD = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    ['X',0,'A']
]
DIR_PAD = [
    ['X', '^', 'A'],
    ['<', 'v', '>']
]

NUM_PAD_DICT = {
    '7': [0, 0],
    '8': [0, 1],
    '9': [0, 2],
    '4': [1, 0],
    '5': [1, 1],
    '6': [1, 2],
    '1': [2, 0],
    '2': [2, 1],
    '3': [2, 2],
    '0': [3, 1],
    'A': [3, 2]
}

DIR_PAD_DICT = {
    '^': [0, 1],
    'A': [0, 2],
    '<': [1, 0],
    'v': [1, 1],
    '>': [1, 2]
}

def GetDirPadInstructionsForNumPad(numCode: str) -> str:
    result = ""
    i = 0
    curPos = NUM_PAD_DICT['A']
    while i < len(numCode):
        targetPos = NUM_PAD_DICT[numCode[i]]
        diff = [targetPos[0] - curPos[0], targetPos[1] - curPos[1]]
        swap = False
        if diff[1] < 0 and curPos[0] == 3 and targetPos[1] == 0:
            swap = True
        if diff[0] > 0 and curPos[1] == 0 and targetPos[0] == 3:
            swap = True
        if swap:
            #Right
            if diff[1] > 0:
                result += '>' * abs(diff[1])
            #Up
            if diff[0] < 0:
                result += '^' * abs(diff[0])
            #Left
            if diff[1] < 0:
                result += '<' * abs(diff[1])
            #Down
            if diff[0] > 0:
                result += 'v' * abs(diff[0])
        else:
            #Left
            if diff[1] < 0:
                result += '<' * abs(diff[1])
            #Down
            if diff[0] > 0:
                result += 'v' * abs(diff[0])
            #Right
            if diff[1] > 0:
                result += '>' * abs(diff[1])
            #Up
            if diff[0] < 0:
                result += '^' * abs(diff[0])
        
        result += 'A'
        i += 1
        curPos = targetPos
    return result

def GetDirPadInstructionsForDirPad(dirCode: str) -> str:
    result = ""
    i = 0
    curPos = DIR_PAD_DICT['A']
    while i < len(dirCode):
        targetPos = DIR_PAD_DICT[dirCode[i]]
        diff = [targetPos[0] - curPos[0], targetPos[1] - curPos[1]]
        #Left
        if diff[1] < 0:
            result += '<' * abs(diff[1])
        #Down
        if diff[0] > 0:
            result += 'v' * abs(diff[0])
        #Right
        if diff[1] > 0:
            result += '>' * abs(diff[1])
        #Up
        if diff[0] < 0:
            result += '^' * abs(diff[0])
        result += 'A'
        i += 1
        curPos = targetPos
    return result

ans = 0
with open("input.txt") as file:
    for line in file:
        numCode = line.strip()
        print("Num code: " + numCode)
        numVal = int(numCode[:-1])
        dirCode1 = GetDirPadInstructionsForNumPad(numCode)
        print("Dir code 1: " + dirCode1)
        dirCode2 = GetDirPadInstructionsForDirPad(dirCode1)
        print("Dir code 2: " + dirCode2)
        dirCode3 = GetDirPadInstructionsForDirPad(dirCode2)
        print("Dir code 3: " + dirCode3)
        print("")
        ans += numVal * len(dirCode3)

print(ans)
