from math import ceil, floor

def hprange(lvl, hp, ev, base):
    n1 = hp - 10 - lvl
    n2 = n1 + 0.99999

    n1 = n1 * 100 / float(lvl) - int(ev/4.0) - (2 * base)
    n2 = n2 * 100 / float(lvl) - int(ev/4.0) - (2 * base)

    n1 = ceil(n1)
    n2 = floor(n2)

    if (n1 > 31):
        n1 = 31
    elif (n1 < 0):
        n1 = 0

    if (n2 > 31):
        n2 = 31
    elif (n2 < 0):
        n2 = 0
    
    return((n1,n2))

def statrange(lvl, value, ev, base, nature):
    n1 = value + 0
    n2 = n1 + 0.99999

    n1 = n1 / nature - 5
    n2 = n2 / nature - 5

    n1 = ceil(n1)
    n2 = floor(n2) + 0.99999

    #print((n1,n2))

    n1 = n1 * 100 / float(lvl) - int(ev/4.0) - (2 * base)
    n2 = n2 * 100 / float(lvl) - int(ev/4.0) - (2 * base)

    n1 = ceil(n1)
    n2 = floor(n2)

    if (n1 > 31):
        n1 = 31
    elif (n1 < 0):
        n1 = 0

    if (n2 > 31):
        n2 = 31
    elif (n2 < 0):
        n2 = 0

    return((n1,n2))
