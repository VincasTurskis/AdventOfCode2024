def breakDownNumber(num: int, parts: list) -> bool:

    if(len(parts) == 1):
        if num == parts[0]:
            return True
        return False

    if num % parts[-1] == 0:
        possibleDivision = breakDownNumber(num / parts[-1], parts[:-1])
        if possibleDivision:
            return possibleDivision

    return breakDownNumber(num - parts[-1], parts[:-1])

sum = 0


with open("input.txt") as file:
    for line in file:

        st = line.strip().split(": ")

        calResult = int(st[0])

        parts = [int(x) for x in st[1].split()]

        if breakDownNumber(calResult, parts):

            sum += calResult
print(sum)

