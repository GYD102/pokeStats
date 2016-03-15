from getStuff import *
from pokemonClass import *

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
    gen = int(input('Enter the generation of the game being played (1 - 7): '))
    stats = getStats(gen)
    evs = getEVs(gen)
    mon = Pokemon(input('Enter the Nickname of the Pokemon to be tracked: '))
    print('\nWe are now tracking %s the %s.\n' % (mon.name, mon.pokemon))
    commands = 'Here are the commands you can input: \n1) "display": displays the stats of the tracked pokemon.\n2) "beat [pokemon species]": updates the EVs based on the Pokemon defeated.\n3) "undo [pokemon species]": undo the "beat" command in case of error.\n4) "lvlup": levels up the tracked pokemon and updates IV ranges.\n5) "write": writes the tracked stats to the tracking file.\n6) "exit": exists the program and automatically writes progress.\n7) "stats [pokemon species]": Display the base stats of the pokemon.\n8) "evyield [pokemon species]": Display the EV yields of the pokemon.\n9) "commands": display these commands again.\n\n'
    print(commands)
    flag = True
    while(flag):
        command = input('Please enter a command: ').split()
        print()
        if command[0] == "display":
            print(mon)
        elif command[0] == "beat":
            try:
                mon.beat(command[1], evs)
            except KeyError:
                print('This is not a valid Pokemon\n')
        elif command[0] == "undo":
            try:
                mon.undo(command[1], evs)
            except KeyError:
                print('This is not a valid Pokemon\n')
        elif command[0] == "lvlup":
            try:
                mon.lvlup([int(x) for x in 
                           input('Please input new stat values separated by spaces '+ 
                                 'in the standard order: ').split()], stats)
            except IndexError:
                print('This is not the correct number of stat values.\n')
            print()
        elif command[0] == "commands":
            print(commands)
        elif command[0] == "write":
            mon.writeFile()
        elif command[0] == "stats":
            try:
                print(stats[command[1]])
            except KeyError:
                print('This is not a valid Pokemon\n')
        elif command[0] == "evyield":
            try:
                print(evs[command[1]])
            except KeyError:
                print('This is not a valid Pokemon\n')
        elif command[0] == "exit":
            flag = False
