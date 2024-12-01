col1 = []
col2 = {}
with open('input.txt') as file:
    for line in file:
        words = line.rstrip().split()
        col1.append(int(words[0]))
        if col2.get(int(words[1])) == None:
            col2[int(words[1])] = 1
        else:
            col2[int(words[1])] += 1
    sum = 0
    for leftNum in col1:
        multiplier = 0
        if leftNum in col2:
            multiplier = leftNum * col2.get(leftNum)
        sum = sum + multiplier
    print(sum)