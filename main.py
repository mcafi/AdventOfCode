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
# centro in 2,3
# diffeast = 2, diffnorth = 3
# 4,6 > 5,1
# diffeast = -2, diffnorth = -3
# 0,0 > -1,2


def rotatewaypoint(dir, degs, east, north, eastship, northship):
    diffeast = east - eastship
    diffnorth = north - northship
    if dir == "L":
        degs = 0 - degs
    if degs == 90:
        return eastship + diffnorth, northship - diffeast
    elif degs == 180:
        return eastship - diffnorth, northship - diffeast
    elif degs == 270:
        return eastship - diffnorth, northship + diffeast
    else:
        return east, north


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

    # s = ship, w = waypoint
    easts = norths = 0
    eastw, northw = 10, 1
    for instruction in instructions:
        dir, val = instruction[0], instruction[1]
        if dir == "N" or dir == "E" or dir == "S" or dir == "W":
            eastw, northw = moveto(dir, eastw, northw, val)
        elif dir == "R" or dir == "L":
            eastw, northw = rotatewaypoint(dir, val, eastw, northw, easts, norths)
        elif dir == "F":
            eastdiff, northdiff = eastw - easts, northw - norths
            eastw += eastdiff * val
            northw += northdiff * val
            easts += eastdiff * val
            norths += northdiff * val
    print(abs(easts) + abs(norths))
