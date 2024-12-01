col1 = []
col2 = []
with open('input.txt') as file:
    for line in file:
        words = line.rstrip().split()
        col1.append(int(words[0]))
        col2.append(int(words[1]))
    col1.sort()
    col2.sort()
    sum = 0
    for leftNum, rightNum in zip(col1, col2):
        sum += abs(leftNum - rightNum)
    print(sum)