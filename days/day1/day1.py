# DAY 1
# Part 1: find two numbers which make 2020 in sum and print their product
# Part 2: find three numbers which make 2020 in sum and print their product

if __name__ == '__main__':
    file = open("./day1.txt", "r")
    lines = file.readlines()
    count = len(lines)

    # Part 1
    for i in range(count):
        for j in range(i + 1, count):
            n1, n2 = int(lines[i]), int(lines[j])
            if n1 + n2 == 2020:
                print(n1 * n2)

    # Part 2
    for i in range(count):
        for j in range(i + 1, count):
            for k in range(j + 1, count):
                n1, n2, n3 = int(lines[i]), int(lines[j]), int(lines[k])
                if n1 + n2 + n3 == 2020:
                    print(n1 * n2 * n3)
