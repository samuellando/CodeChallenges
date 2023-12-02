import sys
with open(sys.argv[1]) as f:
    s = 0
    games = f.readlines()
    for g in games:
        m = {}
        g = g.replace("\n", "")
        pulls = g.split(":")[1].split(";")
        for p in pulls:
            p = p.split(",")
            for group in p:
                color = group.split(" ")[2]
                n = int(group.split(" ")[1])
                if n > m.get(color, 0): 
                    m[color] = n

        s += m.get("red", 0) * m.get("green", 0) * m.get("blue", 0)
    print(s)
