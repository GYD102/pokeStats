from math import ceil, floor

levelMessage = 'Please enter Pokemon level\n'
statMessage = 'Please enter stats in the following format\nHP,AT,DE,SA,SD,SP\n'
evMessage = 'Please enter EVs in the following format\nHP,AT,DE,SA,SD,SP\n'
baseMessage = 'Please enter bases in the following format\nHP,AT,DE,SA,SD,SP\n'
natureMessage = 'Please enter nature in the following format\nHP,AT,DE,SA,SD,SP\n'

lvl = int(input(levelMessage))

statstr = input(statMessage)
statlist = [int(x) for x in statstr.split(',')]

evstr = input(evMessage)
evlist = [int(x) for x in evstr.split(',')]

basestr = input(baseMessage)
baselist = [int(x) for x in basestr.split(',')]

naturestr = input(natureMessage)
naturelist = [float(x) for x in naturestr.split(',')]

#print(statlist)

def hprange(l1, l2, l3):
    hp = l1[0]
    ev = l2[0]
    base = l3[0]

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

def statrange(l1, l2, l3, l4, stat):
# stat is a value from 1 - 5
# 1 -> Attack
# 2 -> Defense
# 3 -> Sp. Attack
# 4 -> Sp. Defense
# 5 -> Speed
    value = l1[stat]
    ev = l2[stat]
    base = l3[stat]
    nature = l4[stat]

    #x = [lvl, value, ev, base, nature]
    #print(x)

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

print('HP   range = ' + str(hprange(statlist, evlist, baselist)))
print('ATTA range = ' + str(statrange(statlist, evlist, baselist, naturelist, 1)))
print('DEFE range = ' + str(statrange(statlist, evlist, baselist, naturelist, 2)))
print('SPAT range = ' + str(statrange(statlist, evlist, baselist, naturelist, 3)))
print('SPDE range = ' + str(statrange(statlist, evlist, baselist, naturelist, 4)))
print('SPEE range = ' + str(statrange(statlist, evlist, baselist, naturelist, 5)))
