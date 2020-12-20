# DAY 13
# Part 1: find the lowest wait but at a given time
# Part 2: find the time where all the bus start subsequently

import re

if __name__ == '__main__':
    file = open("./day13.txt", "r")
    lines = file.readlines()

    # Part 1
    timestamp = int(lines[0])
    buses = {}
    for n in re.findall(r'\d+', lines[1]):
        buses[int(n)] = 0

    for bus in buses:
        while buses[bus] < timestamp:
            buses[bus] += bus

    minbus = list(buses.keys())[0]
    wait = buses[list(buses.keys())[0]] - timestamp

    for bus in buses:
        if buses[bus] - timestamp < wait:
            minbus = bus
            wait = buses[bus] - timestamp

    print(minbus * wait)

    # Part 2
    buses = {}
    diff = 0

    for b in re.findall(r'(\d+|x)', lines[1]):
        if b == 'x':
            diff += 1
            continue
        else:
            buses[int(b)] = diff
            diff += 1

    timestamp = list(buses.keys())[0]
    step = 1
    found = 0

    while True:
        nextbus = list(buses.keys())[found]
        if (timestamp + buses[nextbus]) % nextbus == 0:
            step *= nextbus
            found += 1
            if found == len(buses):
                break
        timestamp += step

    print(timestamp)
