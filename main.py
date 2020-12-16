# This is a sample Python script.
import re
import math

directions = {
    "N": 0,
    "E": 90,
    "S": 180,
    "W": 270
}


def moveto(dir, e, n, l):
    if dir == "N":
        n += l
    elif dir == "E":
        e += l
    elif dir == "S":
        n -= l
    elif dir == "W":
        e -= l
    return e, n


def rotate(dir, rot, degs):
    angle = directions[dir]
    if rot == "L":
        angle -= degs
    elif rot == "R":
        angle += degs
    while angle < 0:
        angle += 360
    while angle >= 360:
        angle -= 360
    for d in directions:
        if directions[d] == angle:
            return d


def rotatee(dir, rot):
    d = ""
    if dir == "N":
        if rot == "L":
            d = "W"
        elif rot == "R":
            d = "E"
    elif dir == "E":
        if rot == "L":
            d = "N"
        elif rot == "R":
            d = "S"
    elif dir == "S":
        if rot == "L":
            d = "E"
        elif rot == "R":
            d = "W"
    elif dir == "W":
        if rot == "L":
            d = "S"
        elif rot == "R":
            d = "N"
    return d


if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()

    instructions = []

    for line in lines:
        ins = re.match(r'([NSEWLRF])(\d+)', line)
        instructions.append([ins.group(1), int(ins.group(2))])

    east = north = 0
    currdir = "E"
    for instruction in instructions:
        dir, val = instruction[0], instruction[1]
        if dir == "N" or dir == "E" or dir == "S" or dir == "W":
            east, north = moveto(dir, east, north, val)
        else:
            if dir == "L" or dir == "R":
                currdir = rotate(currdir, dir, val)
                continue
            east, north = moveto(currdir, east, north, val)

    print(abs(east) + abs(north))
