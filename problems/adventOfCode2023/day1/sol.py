matches = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9"
        ]

toInt = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
        }

with open("input", "r") as f:
    lines = f.readlines()
    s = 0
    for l in lines:
        min = -1
        mins = ""
        max = -1
        maxs = ""
        for match in matches:
            i = l.find(match)
            if i != -1:
                if  min == -1 or i < min:
                    min = i
                    mins = match
            i = l.rfind(match)
            if i != -1:
                if max == -1 or i > max:
                    max = i
                    maxs = match
        n = int(str(toInt[mins]) + str(toInt[maxs]))
        print(l, n)
        s += n

    print(s)

        

