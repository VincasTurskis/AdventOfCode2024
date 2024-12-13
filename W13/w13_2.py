def getMinNumberOfTokens(buttonAVals: tuple, buttonBVals: tuple, target: tuple) -> int:

    increase = 10000000000000
    (AX, AY) = buttonAVals
    (BX, BY) = buttonBVals
    (initX, initY) = target
    tX = initX + increase
    tY = initY + increase

    numOfAPresses = ((tX * BY)-(tY * BX))/((AX * BY)-(AY * BX))
    numOfBPresses = (tX - (AX * numOfAPresses)) / BX
    if numOfAPresses != int(numOfAPresses) or numOfBPresses != int(numOfBPresses):
        return 0
    return (numOfAPresses * 3 + numOfBPresses)

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