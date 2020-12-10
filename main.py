# This is a sample Python script.
import re
import math

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()

    bags = {}
    for line in lines:
        parseLine = re.match(r'(\w+ \w+) bags contain (.*)', line)
        name = parseLine.group(1)
        content = parseLine.group(2)
        print(name, content)
