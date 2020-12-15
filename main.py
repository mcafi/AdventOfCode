# This is a sample Python script.
import re
import math

seats = []
toChange = []


def surroundedbyfree(row, col):
    # top
    if row > 0:
        if seats[row - 1][col] == "#":
            return False
    # left
    if col > 0:
        if seats[row][col-1] == "#":
            return False
    # bottom
    if row < len(seats) - 1:
        if seats[row+1][col] == "#":
            return False
    # right
    if col < len(seats[0]) - 1:
        if seats[row][col+1] == "#":
            return False
    # top left
    if row > 0 and col > 0:
        if seats[row-1][col-1] == "#":
            return False
    # top right
    if row > 0 and col < len(seats[0]) - 1:
        if seats[row-1][col+1] == "#":
            return False
    # bottom left:
    if row < len(seats) - 1 and col > 0:
        if seats[row+1][col-1] == "#":
            return False
    # bottom right:
    if row < len(seats) - 1 and col < len(seats[0]) - 1:
        if seats[row+1][col+1] == "#":
            return False
    return True


def surroundedbyocc(row, col):
    x = 0
    # top
    if row > 0:
        if seats[row-1][col] == "#":
            x += 1
    # left
    if col > 0:
        if seats[row][col-1] == "#":
            x += 1
    # bottom
    if row < len(seats) - 1:
        if seats[row+1][col] == "#":
            x += 1
    # right
    if col < len(seats[0]) - 1:
        if seats[row][col+1] == "#":
            x += 1
    # top left
    if row > 0 and col > 0:
        if seats[row-1][col-1] == "#":
            x += 1
    # top right
    if row > 0 and col < len(seats[0]) - 1:
        if seats[row-1][col+1] == "#":
            x += 1
    # bottom left:
    if row < len(seats) - 1 and col > 0:
        if seats[row+1][col-1] == "#":
            x += 1
    # bottom right:
    if row < len(seats) - 1 and col < len(seats[0]) - 1:
        if seats[row+1][col+1] == "#":
            x += 1
    if x >= 4:
        return True
    else:
        return False


if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()

    for line in lines:
        seats.append(re.findall(r'[\.L]', line))

    while True:
        for s in seats:
            print(" ".join(s))
        print("\n----------\n")
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == "L" and surroundedbyfree(i, j):
                    toChange.append([i, j])
                elif seats[i][j] == "#" and surroundedbyocc(i, j):
                    toChange.append([i, j])
        if len(toChange) > 0:
            for c in toChange:
                if seats[c[0]][c[1]] == "L":
                    seats[c[0]][c[1]] = "#"
                elif seats[c[0]][c[1]] == "#":
                    seats[c[0]][c[1]] = "L"
            toChange = []
        else:
            break

    occupied = 0
    for seatline in seats:
        for seat in seatline:
            if seat == "#":
                occupied += 1
    print(occupied)
