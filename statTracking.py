from natures import nature
from io import UnsupportedOperation
from getStuff import *
from calculations import *

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
        dic = {'name':name}

        dic['pokemon'] = input('This is a new Pokemon. Please enter the pokemon\'s species: ')
        f.write(dic['pokemon']+'\n')
        print('')

        dic['level'] = int(input('Enter the Pokemon\'s level: '))
        f.write(str(dic['level'])+'\n')
        print('')

        nat = input('Enter the Pokemon\'s nature: ')
        f.write(nat+'\n')
        dic['nature'] = nature(nat)
        print('')

        stats = input('Enter the Pokemon\'s stats separated by commas (no spaces):\n')
        dic['stats'] = [int(x) for x in stats.split(',')]
        f.write(stats+'\n')
        print('')

        if input('Is this pokemon freshly caught? (y/n): ')=='y':
            dic['evs'] = [0,0,0,0,0,0]
            f.write('0,0,0,0,0,0\n')
        else:
            evs = input('Enter EVs separated by commas (no spaces):\n')
            dic['evs'] = [int(x) for x in evs.split(',')]
            f.write(evs+'\n')
        print('')

        dic['ivs'] = [(1,31) for x in range(6)]
        f.write('1,31,1,31,1,31,1,31,1,31,1,31\n')
        f.close()
        return dic

class Pokemon:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.pokemon = dictionary['pokemon']
        self.level = dictionary['level']
        self.nature = dictionary['nature']
        self.stats = dictionary['stats']
        self.evs = dictionary['evs']
        self.ivs = dictionary['ivs']

    def __str__(self):
        return (str(self.name)+'\n'+
                str(self.pokemon)+'\n'+
                str(self.level)+'\n'+
                str(self.nature)+'\n'+
                str(self.stats)+'\n'+
                str(self.evs)+'\n'+
                str(self.ivs)+'\n')

    def beat(self, name):
        self.evs = [a+b for a,b in zip(self.evs, evs[name])]

    def lvlup(self, newStats):
        self.level = self.level + 1
        self.stats = newStats
        hp = hprange(self.level, newStats[0], self.evs[0], 
                     stats[self.pokemon][0])
        attackrange = statrange(self.level, newStats[1], self.evs[1], 
                                stats[self.pokemon][1], self.nature[0])
        defenserange = statrange(self.level, newStats[2], self.evs[2], 
                                 stats[self.pokemon][2], self.nature[1])
        spattackrange = statrange(self.level, newStats[3], self.evs[3],
                                  stats[self.pokemon][3], self.nature[2])
        spdefenserange = statrange(self.level, newStats[4], self.evs[4], 
                                   stats[self.pokemon][4], self.nature[3])
        speedrange = statrange(self.level, newStats[5], self.evs[5], 
                               stats[self.pokemon][5], self.nature[4])
        self.ivs = [hp,attackrange,defenserange,spattackrange,
                    spdefenserange,speedrange]

test = Pokemon(parseTrackFile('amg'))
print(test)
test.lvlup([30,30,30,30,30,30])
print(test)
#test.beat('rattata')
#print(test)
#test.addEVs([5,5,5,5,5,5])
#test.name = 'lmao'
#print(test)

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

