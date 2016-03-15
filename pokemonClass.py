from trackFiles import *
from calculations import *
from natures import *

global stats
global evs

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

    def beat(self, name, evs):
        self.evs = [a+b for a,b in zip(self.evs, evs[name])]

    def undo(self, name, evs):
        self.evs = [a-b for a,b in zip(self.evs, evs[name])]

    def lvlup(self, newStats, stats):
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
            statString = statString + str(x) + ' '
        statString = statString[:-1]
        f.write(statString+'\n')

        evString = ''
        for x in self.evs:
            evString = evString + str(x) + ' '
        evString = evString[:-1]
        f.write(evString+'\n')

        ivString = ''
        for x in self.ivs:
            ivString = ivString + str(x[0]) + ' ' + str(x[1]) + ' '
        ivString = ivString[:-1]
        f.write(ivString+'\n')

        f.close()
