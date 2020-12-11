# This is a sample Python script.
import re
import math

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

totalBags = {}


def containsShinyGold(bag):
    bags = totalBags[bag]
    count = 0
    count += bags.count("shiny gold")
    for singleBag in list(set(bags)):
        count += containsShinyGold(singleBag) * bags.count(singleBag)
        print(count, singleBag)
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
        bagsWithGold += containsShinyGold(bag)

    print(bagsWithGold)
