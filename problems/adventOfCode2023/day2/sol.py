max = {
        "red": 12,
        "blue": 14,
        "green": 13,
    }

import sys
with open(sys.argv[1]) as f:
    s = 0
    games = f.readlines()
    for g in games:
        good = True
        g = g.replace("\n", "")
        pulls = g.split(":")[1].split(";")
        for p in pulls:
            p = p.split(",")
            for group in p:
                color = group.split(" ")[2]
                n = int(group.split(" ")[1])
                if n > max[color]:
                    good = False
                    break
            if not good:
                break
        if good:
           s += int(g.split(":")[0].split(" ")[1])


    print(s)
