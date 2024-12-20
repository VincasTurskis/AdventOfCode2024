pattern = "ggrggugwgrrrggrruggurggwguuuuubwrurbgrgbwwwuurg"

with open("input.txt") as file:
    towels = file.readline().strip().split(", ")
    counter = 0
    for towel in towels:
        for i in range(len(pattern)):
            if pattern[i:i+len(towel)] == towel:
                counter += 1
    print(counter)