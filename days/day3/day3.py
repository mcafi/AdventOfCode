# DAY 3
# Part 1: count the tree encountered moving 1 cell down and 3 cell right
# Part 2: count the thee encountered moving down 1 tighe, 1 down 3 rigth, 1 down 5 right, 1 down 7 right, 2 down 1 right

if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()
    maxSize = len(lines[0]) - 1
    trees = x = 0

    # Part 1
    for line in lines:
        if x >= maxSize:
            x -= maxSize
        if line[x] == '#':
            trees += 1
        found = line[x]
        x += 3

    print(trees)
