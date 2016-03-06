from natures import *
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
        dic['nature'] = l[2]
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
        dic['nature'] = nat
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
    def __init__(self, nickname):
        dictionary = parseTrackFile(nickname)
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
        #print(self.level)
        self.level = self.level + 1
        self.stats = newStats
        #print(self.level)
        hp = hprange(self.level, newStats[0], self.evs[0], 
                     stats[self.pokemon][0])
        attackrange = statrange(self.level, newStats[1], self.evs[1], 
                                stats[self.pokemon][1], nature(self.nature)[0])
        defenserange = statrange(self.level, newStats[2], self.evs[2], 
                                 stats[self.pokemon][2], nature(self.nature)[1])
        spattackrange = statrange(self.level, newStats[3], self.evs[3],
                                  stats[self.pokemon][3], nature(self.nature)[2])
        spdefenserange = statrange(self.level, newStats[4], self.evs[4], 
                                   stats[self.pokemon][4], nature(self.nature)[3])
        speedrange = statrange(self.level, newStats[5], self.evs[5], 
                               stats[self.pokemon][5], nature(self.nature)[4])
        oldivs = self.ivs
        self.ivs = [(max(hp[0],oldivs[0][0]),min(hp[1],oldivs[0][1])),
                    (max(attackrange[0],oldivs[1][0]),min(attackrange[1],oldivs[1][1])),
                    (max(defenserange[0],oldivs[2][0]),min(defenserange[1],oldivs[2][1])),
                    (max(spattackrange[0],oldivs[3][0]),min(spattackrange[1],oldivs[3][1])),
                    (max(spdefenserange[0],oldivs[4][0]),min(spdefenserange[1],oldivs[4][1])),
                    (max(speedrange[0],oldivs[5][0]),min(speedrange[1],oldivs[5][1]))]


    def writeFile(self):
        f = open('%s.txt' % self.name, 'w')
        f.write(self.pokemon+'\n')
        f.write(str(self.level)+'\n')
        f.write(self.nature+'\n')
        
        statString = ''
        for x in self.stats:
            statString = statString + str(x) + ','
        statString = statString[:-1]
        f.write(statString+'\n')

        evString = ''
        for x in self.evs:
            evString = evString + str(x) + ','
        evString = evString[:-1]
        f.write(evString+'\n')

        ivString = ''
        for x in self.ivs:
            ivString = ivString + str(x[0]) + ',' + str(x[1]) + ','
        ivString = ivString[:-1]
        f.write(ivString+'\n')
        
        f.close()


#test = Pokemon(parseTrackFile('amg'))
#print(test)
#test.lvlup([30,30,30,30,30,30])
#print(test)
#test.writeFile()
#test = Pokemon(parseTrackFile('amg'))
#print(test)
#test.beat('rattata')
#print(test)
#test.addEVs([5,5,5,5,5,5])
#test.name = 'lmao'
#print(test)

#def commands(string):
'''
beat --pokemonname-- X
lvlup                X
write                X
exit
evolve --into--      Future
'''

#print(parseTrackFile('bulby'))
#print(parseTrackFile('imagine'))

if __name__ == "__main__":
    print('Welcome to Pokemon Stat Tracker v1.0')
    mon = Pokemon(input('Enter the Nickname of the Pokemon to be tracked: '))
    print('\nWe are now tracking %s the %s.\n' % (mon.name, mon.pokemon))
    print('Here are the commands you can input: \n1) "display": displays '+
          'the stats of the tracked pokemon.\n2) "beat [pokemon species]":'+
          ' updates the EVs based on the pokemon defeated.\n3) "lvlup":'+
          ' levels up tracked pokemon and updates IV ranges.\n4) "write":'+
          ' writes the (likely different) tracked stats to the tracking file.'+
          '\n5) "exit": exits the program and automatically writes progress'+
          ' to the tracking file.\n\n')
    flag = True
    while(flag):
        command = input('Please enter a command: ').split()
        print()
        if command[0] == "display":
            print(mon)
        elif command[0] == "beat":
            mon.beat(command[1])
        elif command[0] == "lvlup":
            mon.lvlup([int(x) for x in 
                       input('Please input new stat values separated by spaces '+ 
                             'in the standard order: ').split()])
            print()
        elif command[0] == "write":
            mon.writeFile()
        elif command[0] == "exit":
            flag = False
