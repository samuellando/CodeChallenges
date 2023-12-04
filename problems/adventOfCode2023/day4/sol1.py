import sys
import re

with open(sys.argv[1], "r") as f:
    s = 0
    lines = f.readlines()
    for l in lines:
        card, numbers = l.split(":")
        winning, my = numbers.split("|")

        winning = set(map(lambda x:int(x), re.findall("\d+", winning)))
        my = set(map(lambda x:int(x), re.findall("\d+", my)))

        p = 0
        for n in my:
            if n in winning:
                if p == 0:
                    p = 1
                else:
                    p *= 2

        s += p

    print(s)
