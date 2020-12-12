# DAY 9
# Part 1: find the

def hasSum(group, number):
    found = False
    for i in range(len(group)):
        for j in range(i, len(group)):
            if group[i] + group[j] == number:
                found = True
    return found


def findContinuos(list, number):
    for i in range(len(list)):
        x = 0
        for j in range(i, len(list)):
            x += list[j]
            if x > number:
                break
            if x == number:
                min = max = list[i]
                for k in range(i, j+1):
                    if list[k] < min:
                        min = list[k]
                    if list[k] > max:
                        max = list[k]
                return min + max


if __name__ == '__main__':
    file = open("./day9.txt", "r")
    lines = file.readlines()

    numbers = []
    for line in lines:
        numbers.append(int(line))

    preamble = 25
    group = numbers[0:preamble]
    error = 0
    for i in range(preamble, len(numbers)):
        if not hasSum(group, numbers[i]):
            error = int(lines[i])
            break
        group.append(numbers[i])
        group.pop(0)
    print(error)

    print(findContinuos(numbers, error))
