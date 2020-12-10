# DAY 6
# Part 1: find how many answers have been answered by at least one person of every group
# part 2: find how many answers have been answered by every person of every group

if __name__ == '__main__':
    file = open("./day6.txt", "r")
    lines = file.readlines()

    # Part 1
    answersCount = 0
    groups = []
    group = []
    for line in lines:
        if line != "\n":
            for char in line:
                if char != "\n":
                    group.append(char)
        else:
            groups.append(set(group))
            group = []
    # add the last group
    groups.append(set(group))
    for group in groups:
        answersCount += len(group)
    print(answersCount)

    # Part 2
    answersCount = 0
    groups = []
    group = []
    for line in lines:
        if line != "\n":
            person = []
            for char in line:
                if char != "\n":
                    person.append(char)
            group.append(person)
        else:
            groups.append(group)
            group = []
    # add the last group
    groups.append(group)
    for group in groups:
        answers = 0
        groupSize = len(group)
        # since all the people in the groups need to have chosen the answer, i can just check the first
        firstPerson = group[0]
        for c in firstPerson:
            singleAnswer = 0
            for person in group:
                if person.count(c) > 0:
                    singleAnswer += 1
            if singleAnswer == groupSize:
                answers += 1
        answersCount += answers
    print(answersCount)
