# DAY 7
# Part 1: count the bags which eventually contain a "shiny gold" bag

import re

totalBags = {}


# for part 1, count the "shiny gold" bags inside a bag
def countShinyGold(bag):
    bags = totalBags[bag]
    count = 0
    count += bags.count("shiny gold")
    for singleBag in list(set(bags)):
        count += countShinyGold(singleBag) * bags.count(singleBag)
    return count


# for part 2, count the total bags inside a bag
def countTotalBags(bag):
    bags = totalBags[bag]
    count = 0
    count += len(bags)
    for singleBag in bags:
        count += countTotalBags(singleBag)
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("day7.txt", "r")
    lines = file.readlines()

    # initial setup, common for both parts
    bagsWithGold = 0
    for line in lines:
        parseLine = re.match(r'(\w+ \w+) bags contain (.*)', line)
        name = parseLine.group(1)
        content = parseLine.group(2)
        bagContent = []
        if content == "no other bags.":
            bagContent = []
        else:
            parseContent = re.findall(r'(\d \w+ \w+)', content)
            for contentString in parseContent:
                parseContentString = re.match(r'(\d) (\w+ \w+)', contentString)
                for i in range(0, int(parseContentString.group(1))):
                    bagContent.append(parseContentString.group(2))
        totalBags[name] = bagContent

    # Part 1
    for bag in totalBags:
        if countShinyGold(bag) > 0:
            bagsWithGold += 1
    print(bagsWithGold)

    # Part 2
    print(countTotalBags("shiny gold"))
