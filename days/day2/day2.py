# DAY 2
# Part 1, check if the

import re


def hasChar(string, index, ch):
    if len(string) < index:
        return False
    return string[index - 1] == ch


if __name__ == '__main__':
    file = open("./day2.txt", "r")
    lines = file.readlines()

    # part 1
    valid = 0
    for line in lines:
        parser = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        minChar, maxChar, char, password = int(parser.group(1)), int(parser.group(2)), parser.group(3), parser.group(4)
        count = 0
        for c in password:
            if c == char:
                count += 1
        if minChar <= count <= maxChar:
            valid += 1
    print(valid)

    # part 2
    valid = 0
    for line in lines:
        parser = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        lowerChar, upperChar, char, password = int(parser.group(1)), int(parser.group(2)), parser.group(3), parser.group(4)
        hasLower, hasUpper = hasChar(password, lowerChar, char), hasChar(password, upperChar, char)
        if hasLower ^ hasUpper:
            valid += 1
    print(valid)
