import functools

@functools.cache
def calculateSecretNumber(initNumber: int) -> int:
    num = ((initNumber * 64) ^ initNumber) % 16777216
    num = ((num // 32) ^ num) % 16777216
    return ((num * 2048) ^ num) % 16777216

ITERATIONS = 2000

sum = 0
counter = 0
with open("input.txt") as file:
    for line in file:
        counter += 1

        if counter % 50 == 0:
            print(counter)

        number = int(line.strip())
        for i in range(ITERATIONS):
            number = calculateSecretNumber(number)
        sum += number

print(sum)