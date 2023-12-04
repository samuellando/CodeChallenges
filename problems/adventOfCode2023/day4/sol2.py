import sys
import re

with open(sys.argv[1], "r") as f:
    s = 0
    copies = {}
    lines = f.readlines()
    for l in lines:
        card, numbers = l.split(":")
        winning, my = numbers.split("|")

        card = int(re.findall("\d+", card)[0])

        winning = set(map(lambda x:int(x), re.findall("\d+", winning)))
        my = set(map(lambda x:int(x), re.findall("\d+", my)))

        p = 0
        for n in my:
            if n in winning:
                p += 1

        for _ in range(copies.get(card, 0) + 1):
            s += 1
            for i in range(p): 
                copies[card + i + 1] = copies.get(card + i + 1, 0) + 1

    print(s)
