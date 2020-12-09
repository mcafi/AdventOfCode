# This is a sample Python script.
import re
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()
    maxSize = len(lines[0]) - 1
    trees = x = 0
    found = "-"

    for line in lines:
        if x >= maxSize:
            x -= maxSize
        if line[x] == '#':
            trees += 1
        found = line[x]
        x += 3

    print(trees)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
