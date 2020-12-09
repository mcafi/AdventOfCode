# This is a sample Python script.
import re
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()
    maxSize = len(lines[0])
    print(maxSize)
    trees = 0

    for line in lines:
        print(line)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
