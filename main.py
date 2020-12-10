# This is a sample Python script.
import re
import math

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()

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

    seats.sort()
    firstSeat = seats[0]
    for seat in seats:
        if seat != seats[seat - firstSeat]:
            # this means i passed over my seat
            print(seat - 1)
            break
