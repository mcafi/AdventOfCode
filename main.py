# This is a sample Python script.
import re
import math


if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()

    timestamp = int(lines[0])
    buses = {}
    for n in re.findall(r'\d+', lines[1]):
        buses[int(n)] = 0

    for bus in buses:
        while buses[bus] < timestamp:
            buses[bus] += bus

    print(buses)
    min = list(buses.keys())[0]
    wait = buses[list(buses.keys())[0]] - timestamp

    for bus in buses:
        if buses[bus] - timestamp < wait:
            min = bus
            wait = buses[bus] - timestamp

    print(min * wait)
