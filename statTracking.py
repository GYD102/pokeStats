from getStuff import *
from pokemonClass import *
import os

# Command descriptions:
beat = "[nickname] beat [species]\n    Updates [nickname]'s EVs after defeating a [species].\n"
display = "display [nickname]\n    Displays the current tracking information of [nickname].\n"
evyield = "evyield [species]\n    Displays the EVs yielded by [species].\n"
ex = "exit\n    Exits the tracking program WITHOUT writing tracking data to tracking file.\n"
hlp = "help ([command])\n    Displays usage information about [command] or about all commands if one isn't specified.\n"
lvlup = "lvlup [nickname]\n    Updates tracking information, recalculates IV ranges.\n"
stats = "stats [species]\n    Displays the base stats of [species].\n"
track = "track [nickname]\n    Adds [nickname] to the list of Pokemon being tracked.\n"
trackng = "tracking\n    Displays list of all Pokemon currently being tracked.\n"
undo = "[nickname] undo [species]\n    Removes EVs yielded by [species] to [nickname].\n"
untrack = "untrack [nickname]\n    Removes [nickname] from list of Pokemon being tracked.\n"
write = "write [nickname]\n    Write tracking information to [nickname]'s tracking file.\n"

invPok = "This is not a valid Pokemon."

commands = beat + display + evyield + ex + hlp + lvlup + stats + track + trackng + undo + untrack + write

if __name__ == "__main__":
    print('Welcome to Pokemon Stat Tracker v1.0')
    gen = int(input('Enter the generation of the game being played (1 - 7): '))
    stats = getStats(gen)
    evs = getEVs(gen)
    tracking = {}
    flag = True
    while(flag):
        command = input('>>> ').split()
        #print()
        if len(command) == 1:
            if command[0] == "clear":
                os.system('clear')
            elif command[0] == "exit":
                flag = False
            elif command[0] == "help":
                print(commands)
            elif command[0] == "tracking":
                print(list(tracking.keys()))
        elif command[1] == "beat":
            try:
                tracking[command[0]].beat(command[2], evs)
            except KeyError:
                print(invPok)
        elif command[0] == "display":
            try:
                print(tracking[command[1]])
            except KeyError:
                print("This Pokemon is not currently being tracked.")
        elif command[0] == "evyield":
            try:
                print(evs[command[1]])
            except KeyError:
                print(invPok)
        elif command[0] == "help":
            if command[1] == "beat":
                print(beat)
            elif command[1] == "display":
                print(display)
            elif command[1] == "evyield":
                print(evyield)
            elif command[1] == "exit":
                print(ex)
            elif command[1] == "help":
                print(hlp)
            elif command[1] == "lvlup":
                print(lvlup)
            elif command[1] == "stats":
                print(stats)
            elif command[1] == "track":
                print(track)
            elif command[1] == "tracking":
                print(trackng)
            elif command[1] == "undo":
                print(undo)
            elif command[1] == "untrack":
                print(untrack)
            elif command[1] == "write":
                print(write)
            else:
                print("This is not a valid command.")
        elif command[0] == "lvlup":
            try:
                tracking[command[1]].lvlup([int(x) for x in 
                           input('Please input new stat values separated by spaces '+ 
                                 'in the standard order: ').split()], stats)
            except IndexError:
                print('This is not the correct number of stat values.\n')
            except KeyError:
                print('This Pokemon is not being tracked.\n')
        elif command[0] == "stats":
            try:
                print(stats[command[1]])
            except KeyError:
                print(invPok)
        elif command[0] == "track":
            tracking[command[1]] = Pokemon(command[1])
        elif command[1] == "undo":
            try:
                tracking[command[0]].undo(command[2], evs)
            except KeyError:
                print(invPok)
        elif command[0] == "untrack":
            try:
                del tracking[command[1]]
            except KeyError:
                print("This Pokemon is not currently being tracked.")
        elif command[0] == "write":
            try:
                tracking[command[1]].writeFile()
            except KeyError:
                print("This Pokemon is not currently being tracked.")
