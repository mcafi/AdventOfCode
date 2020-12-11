# DAY 8
# Part 1: find the acc value when reaching an instruction for the second time
# Part 2: find the acc value after fixing one of the jmp or nop

import re


if __name__ == '__main__':
    file = open("./day8.txt", "r")
    lines = file.readlines()

    # Part 1
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

    # Part 2
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
                currentFix = i
                fixes.append(i)
                i += 1
        elif instruction == "nop":
            if i in fixes or currentFix is not None:
                i += 1
            else:
                currentFix = i
                fixes.append(i)
                i += value
    print(acc)
