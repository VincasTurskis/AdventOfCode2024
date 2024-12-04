import re


sum = 0
with open('input.txt') as file:
    for line in file:
        mulCommands = re.findall("mul\([0-9]+,[0-9]+\)", line)
        for command in mulCommands:
            nums = re.findall("[0-9]+", command)
            sum += (int(nums[0]) * int(nums[1]))
print(sum)