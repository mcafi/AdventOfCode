# DAY 11
# Part 1: arrange people in seats checking the 8 surrounding seats
# Part 2: arrange people in seats checking the 8 directions around each seat

import re

seats = []


# function for part 1
def occupiednearby(row, col):
    count = 0
    # top
    if row > 0:
        if seats[row-1][col] == "#":
            count += 1
    # left
    if col > 0:
        if seats[row][col-1] == "#":
            count += 1
    # bottom
    if row < len(seats) - 1:
        if seats[row+1][col] == "#":
            count += 1
    # right
    if col < len(seats[0]) - 1:
        if seats[row][col+1] == "#":
            count += 1
    # top left
    if row > 0 and col > 0:
        if seats[row-1][col-1] == "#":
            count += 1
    # top right
    if row > 0 and col < len(seats[0]) - 1:
        if seats[row-1][col+1] == "#":
            count += 1
    # bottom left
    if row < len(seats) - 1 and col > 0:
        if seats[row+1][col-1] == "#":
            count += 1
    # bottom right
    if row < len(seats) - 1 and col < len(seats[0]) - 1:
        if seats[row+1][col+1] == "#":
            count += 1
    return count


# function for part 2
def occupieddiag(row, col):
    count = 0
    # top
    x, y = col, row
    while y > 0:
        visible = seats[y-1][x]
        if visible == "#":
            count += 1
            break
        elif visible == "L":
            break
        else:
            y -= 1
    # left
    x, y = col, row
    while x > 0:
        visible = seats[y][x-1]
        if visible == "#":
            count += 1
            break
        elif visible == "L":
            break
        else:
            x -= 1
    # bottom
    x, y = col, row
    while y < len(seats) - 1:
        visible = seats[y+1][x]
        if visible == "#":
            count += 1
            break
        elif visible == "L":
            break
        else:
            y += 1
    # right
    x, y = col, row
    while x < len(seats[0]) - 1:
        visible = seats[y][x+1]
        if visible == "#":
            count += 1
            break
        elif visible == "L":
            break
        else:
            x += 1
    # top left
    x, y = col, row
    while x > 0 and y > 0:
        visible = seats[y-1][x-1]
        if visible == "#":
            count += 1
            break
        elif visible == "L":
            break
        else:
            x -= 1
            y -= 1
    # top right
    x, y = col, row
    while x < len(seats[0]) - 1 and y > 0:
        visible = seats[y-1][x+1]
        if visible == "#":
            count += 1
            break
        elif visible == "L":
            break
        else:
            x += 1
            y -= 1
    # bottom left
    x, y = col, row
    while x > 0 and y < len(seats) - 1:
        visible = seats[y+1][x-1]
        if visible == "#":
            count += 1
            break
        elif visible == "L":
            break
        else:
            x -= 1
            y += 1
    # bottom right
    x, y = col, row
    while x < len(seats[0]) - 1 and y < len(seats) - 1:
        visible = seats[y+1][x+1]
        if visible == "#":
            count += 1
            break
        elif visible == "L":
            break
        else:
            x += 1
            y += 1
    return count


if __name__ == '__main__':
    file = open("day11.txt", "r")
    lines = file.readlines()

    # Part 1
    for line in lines:
        seats.append(re.findall(r'[\.L]', line))

    toChange = []
    while True:
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == "L" and occupiednearby(i, j) == 0:
                    toChange.append([i, j])
                elif seats[i][j] == "#" and occupiednearby(i, j) >= 4:
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

    # Part 2
    seats = []
    toChange = []
    for line in lines:
        seats.append(re.findall(r'[\.L]', line))

    while True:
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == "L" and occupieddiag(i, j) == 0:
                    toChange.append([i, j])
                elif seats[i][j] == "#" and occupieddiag(i, j) >= 5:
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
