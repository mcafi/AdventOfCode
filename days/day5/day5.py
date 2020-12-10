# DAY 5
# Part 1: find the highest seat ID on the plane
# Part 2: find the missing ID between the seats

import re
import math

if __name__ == '__main__':
    file = open("day5.txt", "r")
    lines = file.readlines()

    # Part 1
    seats = []
    highestId = 0
    for line in lines:
        row = col = 0
        if re.match(r'^[FB]{7}[LR]{3}$', line):
            for i in range(7):
                if line[i] == 'B':
                    row += math.pow(2, 7 - (i + 1))
            for i in range(7, 10):
                if line[i] == 'R':
                    col += math.pow(2, 10 - (i + 1))
        seatId = (int(row) * 8) + int(col)
        seats.append(seatId)
        if seatId > highestId:
            highestId = seatId
    print(highestId)

    # Part 2
    seats.sort()
    firstSeat = seats[0]
    for seat in seats:
        if seat != seats[seat - firstSeat]:
            # this means i passed over my seat
            print(seat - 1)
            break
