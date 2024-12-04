import re


sum = 0
shouldCount = True
with open('input.txt') as file:
    for line in file:
        mulCommands = re.findall("(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))", line)
        print(mulCommands)
        for command in mulCommands:
            (mult, do, dont) = command
            if do == "do()":
                shouldCount = True
            elif dont == "don't()":
                shouldCount = False
            elif shouldCount:
                nums = re.findall("[0-9]+", mult)
                sum += (int(nums[0]) * int(nums[1]))
print(sum)