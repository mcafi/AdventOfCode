# This is a sample Python script.
import re
import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()

    adapters = []
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
