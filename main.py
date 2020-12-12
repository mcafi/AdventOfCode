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
    print(adapters)
