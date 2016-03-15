from io import UnsupportedOperation

def getTrackFile(name):
    try:
        return open(('%s.txt' % name),'r')
    except FileNotFoundError:
        return open(('%s.txt' % name),'w')

def createTrackFile(name):
    f = getTrackFile(name)
    dic = {'name':name}

    dic['pokemon'] = input('This is a new Pokemon. Please enter the pokemon\'s species: ')
    f.write(dic['pokemon']+'\n')
    print('')

    dic['level'] = int(input('Enter the Pokemon\'s level: '))
    f.write(str(dic['level'])+'\n')
    print('')

    nat = input('Enter the Pokemon\'s nature: ')
    f.write(nat+'\n')
    dic['nature'] = nat
    print('')

    tempstats = input('Enter the Pokemon\'s stats separated by spaces:\n')
    dic['stats'] = [int(x) for x in tempstats.split()]
    f.write(tempstats+'\n')
    print('')

    if input('Is this pokemon freshly caught? (y/n): ')=='y':
        dic['evs'] = [0,0,0,0,0,0]
        f.write('0 0 0 0 0 0\n')
    else:
        tempevs = input('Enter EVs separated by spaces:\n')
        dic['evs'] = [int(x) for x in tempevs.split()]
        f.write(tempevs+'\n')
    print('')

    dic['ivs'] = [(1,31) for x in range(6)]
    f.write('1 31 1 31 1 31 1 31 1 31 1 31\n')
    f.close()
    return dic

def parseTrackFile(name):
    f = getTrackFile(name)
    try:
        s = f.read()
        l = s.splitlines()
        f.close()
        #print(l)
        dic = {'name':name}
        dic['pokemon'] = l[0]
        dic['level'] = int(l[1])
        dic['nature'] = l[2]
        dic['stats'] = [int(x) for x in l[3].split()]
        dic['evs'] = [int(x) for x in l[4].split()]
        l5 = [int(x) for x in l[5].split()]
        #print(l5)
        #print(type(len(l5)))
        #for i in range(len(l5)/2):
        #    print(i)
        dic['ivs'] = [(l5[i*2], l5[i*2+1]) for i in range(len(l5)//2)]
        return dic
    except UnsupportedOperation:
        createTrackFile(name)

