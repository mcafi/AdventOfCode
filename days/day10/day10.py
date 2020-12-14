# DAY 10
# Part 1: find the number of 1-jumps and 3-jumps to connect the device with the adapters
# Part 2: find the total number of possible connections using all my adapters

if __name__ == '__main__':
    file = open("./day10.txt", "r")
    lines = file.readlines()

    adapters = [0]
    for line in lines:
        adapters.append(int(line))
    adapters.sort()

    # considering the outlet (0) and my device as adapters since they'll connect

    last = adapters[len(adapters) - 1]
    device = last + 3
    adapters.append(device)

    # Part 1
    jump1 = 0
    jump3 = 0
    curr = 0

    while curr != device:
        if curr + 1 in adapters:
            jump1 += 1
            curr += 1
        else:
            jump3 += 1
            curr += 3

    print(jump1 * jump3)

    #Part 2
    choices = []
    consecutive = 1
    for a in adapters:
        if a + 1 not in adapters:
            if consecutive == 3:
                choices.append(2)
            elif consecutive == 4:
                choices.append(4)
            elif consecutive == 5:
                choices.append(7)
            consecutive = 1
        else:
            consecutive += 1

    result = 1
    for choice in choices:
        result *= choice

    print(result)
