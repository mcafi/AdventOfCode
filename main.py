# This is a sample Python script.
import re
import math

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()

    acc = 0
    executed = []
    i = 0
    while i < len(lines):
        if i in executed:
            break
        executed.append(i)
        line = lines[i]
        regex = re.match(r'(acc|jmp|nop) ([+-]\d+)', line)
        instruction, value = regex.group(1), int(regex.group(2))
        if instruction == "acc":
            acc += value
            i += 1
        elif instruction == "jmp":
            i += value
        else:
            i += 1
    print(acc)

    acc = 0
    executed = []
    fixes = []
    currentFix = None
    i = 0
    while i < len(lines):
        if i in executed:
            executed = []
            acc = 0
            i = 0
            currentFix = None
        executed.append(i)
        line = lines[i]
        regex = re.match(r'(acc|jmp|nop) ([+-]\d+)', line)
        instruction, value = regex.group(1), int(regex.group(2))
        if instruction == "acc":
            acc += value
            i += 1
        elif instruction == "jmp":
            if i in fixes or currentFix is not None:
                i += value
            else:
                print("fixing... ", i)
                currentFix = i
                fixes.append(i)
                i += 1
        elif instruction == "nop":
            if i in fixes or currentFix is not None:
                i += 1
            else:
                print("fixing... ", i)
                currentFix = i
                fixes.append(i)
                i += value
    print(acc)
