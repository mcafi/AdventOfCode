# DAY 12
# Part 1: calculate the position of the ship moving it according to instructions
# Part 2: calculate the positions of the ship moving the waypoint according to instructions

import re

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


def rotatewaypoint(dir, degs, east, north):
    if dir == "L":
        degs = 360 - degs
    if degs == 90:
        return north, -east
    elif degs == 180:
        return -east, -north
    elif degs == 270:
        return -north, east
    else:
        return east, north


if __name__ == '__main__':
    file = open("day12.txt", "r")
    lines = file.readlines()

    instructions = []
    for line in lines:
        ins = re.match(r'([NSEWLRF])(\d+)', line)
        instructions.append([ins.group(1), int(ins.group(2))])

    # Part 1
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

    # Part 2
    east = north = 0
    eastway, northway = 10, 1
    for instruction in instructions:
        dir, val = instruction[0], instruction[1]
        if dir == "N" or dir == "E" or dir == "S" or dir == "W":
            eastway, northway = moveto(dir, eastway, northway, val)
        elif dir == "R" or dir == "L":
            eastway, northway = rotatewaypoint(dir, val, eastway, northway)
        elif dir == "F":
            east += eastway * val
            north += northway * val
    print(abs(east) + abs(north))
