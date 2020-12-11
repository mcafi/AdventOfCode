# This is a sample Python script.
import re
import math

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

totalBags = {}


def containsBag(bagList, bag):
    bags = totalBags[bagList]
    contains = False
    if bags.count(bag) > 0:
        return True
    for singleBag in list(set(bags)):
        containsBag(singleBag, bag)
    return contains


def countTotalBags(bag):
    bags = totalBags[bag]
    count = 0
    count += len(bags)
    for singleBag in bags:
        count += countTotalBags(singleBag)
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("inputs.txt", "r")
    lines = file.readlines()

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

    currentBag = 0
    for bag in totalBags:
        currentBag += 1
        print("Valigia ", currentBag, " di ", len(totalBags), "...")
        if containsBag(bag, "shiny gold"):
            bagsWithGold += 1

    print(bagsWithGold)

    print(countTotalBags("shiny gold"))
