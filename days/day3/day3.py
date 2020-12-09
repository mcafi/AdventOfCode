# DAY 3
# Part 1: count the tree encountered moving 1 cell down and 3 cell right
# Part 2: count the thee encountered moving down 1 right, 1 down 3 right, 1 down 5 right, 1 down 7 right, 2 down 1 right

if __name__ == '__main__':
    file = open("./day3.txt", "r")
    lines = file.readlines()
    maxSize = len(lines[0]) - 1
    trees = x = 0

    # Part 1
    for line in lines:
        if x >= maxSize:
            x -= maxSize
        if line[x] == '#':
            trees += 1
        x += 3
    print(trees)

    # Part 2
    # ty variables counting trees, where y is a = 1r1d, b = 3r1d, c = 5r1d, d = 7r1d, e = 2d1r
    # xn variables where x is the right shift amount
    ta = tb = tc = td = te = x1 = x3 = x5 = x7 = 0
    for i, line in enumerate(lines):
        if x1 >= maxSize:
            x1 -= maxSize
        if x3 >= maxSize:
            x3 -= maxSize
        if x5 >= maxSize:
            x5 -= maxSize
        if x7 >= maxSize:
            x7 -= maxSize
        if line[x1] == '#':
            ta += 1
            if i % 2 == 0:
                te += 1
        if line[x3] == "#":
            tb += 1
        if line[x5] == "#":
            tc += 1
        if line[x7] == "#":
            td += 1
        x1 += 1
        x3 += 3
        x5 += 5
        x7 += 7
    print(ta * tb * tc * td * te)
