def getMinNumberOfTokens(buttonAVals: tuple, buttonBVals: tuple, target: tuple) -> int:
    minTokens = 10000
    (bAX, bAY) = buttonAVals
    (bBX, bBY) = buttonBVals
    (tX, tY) = target
    for i in range(0, 101):
        remX = tX - (bBX * i)
        if remX % bAX == 0:
            ACount = int(remX / bAX)
            if bAY * ACount + bBY * i == tY:
                if ACount * 3 + i < minTokens:
                    minTokens = ACount * 3 + i
    if minTokens == 10000:
        return 0
    return minTokens

tokenSum = 0
with open("input.txt") as file:
    line = file.readline()
    while True:
        if not line:
            break
        A_vals = line.strip().split(": ")[1]
        valA_X = int(A_vals.split(", ")[0][2:])
        valA_Y = int(A_vals.split(", ")[1][2:])
        buttonAVals = (valA_X, valA_Y)
        line = line = file.readline()
        B_vals = line.strip().split(": ")[1]
        valB_X = int(B_vals.split(", ")[0][2:])
        valB_Y = int(B_vals.split(", ")[1][2:])
        buttonBVals = (valB_X, valB_Y)
        line = file.readline()
        targetVals = line.strip().split(": ")[1]
        target_X = int(targetVals.split(", ")[0][2:])
        target_Y = int(targetVals.split(", ")[1][2:])
        target = (target_X, target_Y)
        tokenSum += getMinNumberOfTokens(buttonAVals, buttonBVals, target)
        line = file.readline()
        line = file.readline()
print(tokenSum)