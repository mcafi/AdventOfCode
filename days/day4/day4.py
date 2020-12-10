# DAY 4
# Part 1: count all the passports which have all the required fields set
# Part 2: count all the passports which have all the required fields set and correct

import re

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # cid is optional
colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def checkvalidpassport(passport):
    if all(key in passport for key in fields):

        if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
            return False

        if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
            return False

        if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
            return False

        heightReg = re.match(r'([0-9]*)([a-z]*)', passport["hgt"])
        unit, height = heightReg.group(2), int(heightReg.group(1))
        if unit == "cm":
            if height < 150 or height > 193:
                return False
        elif unit == "in":
            if height < 59 or height > 76:
                return False
        else:
            return False

        if not re.match(r'^#[0-9a-f]{6}$', passport["hcl"]):
            return False

        if passport["ecl"] not in colors:
            return False

        if not re.match(r'^[0-9]{9}$', passport["pid"]):
            return False

        return True

    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("day5.txt", "r")
    lines = file.readlines()
    values = []

    # Part 1
    validPassports = 0
    for line in lines:
        if line != "\n":
            values.extend(line.split(" "))
        else:
            passport = {}
            for value in values:
                parser = re.match(r'([a-z]{3}):(.+)', value)
                passport[parser.group(1)] = parser.group(2)
            if all(key in passport for key in fields):
                validPassports += 1
            values = []
    print(validPassports)

    # Part 2
    validPassports = 0
    for line in lines:
        if line != "\n":
            values.extend(line.split(" "))
        else:
            passport = {}
            for value in values:
                parser = re.match(r'([a-z]{3}):(.+)', value)
                passport[parser.group(1)] = parser.group(2)
            if checkvalidpassport(passport):
                validPassports += 1
            values = []
    print(validPassports)
