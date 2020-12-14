# This is a sample Python script.
import re
import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()

    adapters = [0]
    for line in lines:
        adapters.append(int(line))
    adapters.sort()

    last = adapters[len(adapters) - 1]

    device = last + 3

    jump1 = 0
    jump3 = 1  # i know the last jump is +3
    curr = 0

    while curr != last:
        if curr + 1 in adapters:
            jump1 += 1
            curr += 1
        else:
            jump3 += 1
            curr += 3

    print(jump1 * jump3)

    choices = []
    consecutive = 1
    for a in adapters:
        if a + 1 not in adapters:
            if consecutive == 3:
                choices.append(2)
            elif consecutive == 4:
                choices.append(4)
            elif consecutive == 5:
                choices.append(7)
            consecutive = 1
        else:
            consecutive += 1

    result = 1
    for choice in choices:
        result *= choice

    print(result)
