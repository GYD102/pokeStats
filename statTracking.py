from natures import nature
from io import UnsupportedOperation
from getStuff import *

evs = getEVs()
stats = getStats()

#print(evs['charmander'])
#print(stats['bulbasaur'])

def getTrackFile(name):
    try:
        return open(('%s.txt' % name),'r')
    except FileNotFoundError:
        return open(('%s.txt' % name),'w')

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
        dic['nature'] = nature(l[2])
        dic['stats'] = [int(x) for x in l[3].split(',')]
        dic['evs'] = [int(x) for x in l[4].split(',')]
        l5 = [int(x) for x in l[5].split(',')]
        #print(l5)
        #print(type(len(l5)))
        #for i in range(len(l5)/2):
        #    print(i)
        dic['ivs'] = [(l5[i*2], l5[i*2+1]) for i in range(len(l5)//2)]
        return dic
    except UnsupportedOperation:
        f.close()
        dic = {'name':name}
        dic['pokemon'] = input('This is a new Pokemon. Please enter the pokemon\'s species: ')
        print('')
        dic['level'] = int(input('Enter the Pokemon\'s level: '))
        print('')
        dic['nature'] = nature(input('Enter the Pokemon\'s nature: '))
        print('')
        stats = input('Enter the Pokemon\'s stats separated by commas (no spaces):\n')
        dic['stats'] = [int(x) for x in stats.split(',')]
        print('')
        if input('Is this pokemon freshly caught? (y/n): ')=='y':
            dic['evs'] = [0,0,0,0,0,0]
        else:
            dic['evs'] = [int(x) for x in input('Enter EVs separated by commas (no spaces):\n').split(',')]
        print('')
        dic['ivs'] = [(1,31) for x in range(6)]
        return dic



def beat(dic, name):
    dic['evs'] = [a+b for a,b in zip(dic['evs'],evs[name])]
    



#def commands(string):
    '''
    beat --pokemonname--
    lvlup
    write
    exit
    evolve --into--
    '''

#print(parseTrackFile('bulby'))
#print(parseTrackFile('imagine'))

