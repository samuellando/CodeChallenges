"""
Get all the numbers (n, y, xstart, xend)
Get all the symbols (y, x)
For each symobl check if there is a adgecent number
"""

import sys
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    
    numbers = {}
    for y, l in enumerate(lines):
        xstart = -1
        xend = -1
        for x, c in enumerate(l):
            if c.isdigit():
                if xstart == -1:
                    xstart = x
                xend = x
            else:
                if xstart != -1:
                    n = int(l[xstart:xend+1])
                    numbers[y] = numbers.get(y, []) + [[n, xstart, xend]]
                    xstart = -1
                    xend = -1

    gears = []
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "*":
                gears.append((y,x))

    sum = 0
    for y, x in gears :
        adj = []
        for yp in range(y-1, y+2):
            for i, v in enumerate(numbers.get(yp, [])):
                xstart = v[1]
                xend = v[2]
                n = v[0]
                if x >= xstart - 1 and x <= xend + 1:
                    adj.append(n)

        if len(adj) == 2:
            sum += adj[0] * adj[1]
                    
    print(sum)
