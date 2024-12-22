import functools

@functools.cache
def calculateSecretNumber(initNumber: int) -> int:
    num = ((initNumber * 64) ^ initNumber) % 16777216
    num = ((num // 32) ^ num) % 16777216
    return ((num * 2048) ^ num) % 16777216

ITERATIONS = 2000

price_sequences_dict = dict()
cur_num_sequences_dict = dict()

counter = 0
with open("input.txt") as file:
    for line in file:
        cur_num_sequences_dict = dict()

        counter += 1
        if counter % 50 == 0:
            print(counter)

        number = int(line.strip())
        prevNumber = 0
        curDiffSequence = tuple()
        diff = 0
        for i in range(ITERATIONS):
            prevNumber = number
            number = calculateSecretNumber(number)
            diff = (number % 10) - (prevNumber % 10)
            curDiffSequence = (*curDiffSequence, diff)
            if len(curDiffSequence) > 4:
                curDiffSequence = curDiffSequence[1:]
            if len(curDiffSequence) == 4:
                if curDiffSequence not in cur_num_sequences_dict.keys():
                    cur_num_sequences_dict[curDiffSequence] = (number % 10)
        for seq in cur_num_sequences_dict.keys():
            price_sequences_dict[seq] = price_sequences_dict.get(seq, 0) + cur_num_sequences_dict[seq]
    
maxVal = 0
maxKey = ""
for val in price_sequences_dict.keys():
    if maxVal < price_sequences_dict[val]:
        maxVal = price_sequences_dict[val]
        maxKey = val

print(maxVal)
print(maxKey)

