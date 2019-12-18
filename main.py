from bestPkmToChoose import findPKMToFight
from calculateBestDPS import compareAllDPS
import time
from dataFromPokedex import readCSV
'''This file has functions that actually runs the program and ask users for input.'''


pokedexData = readCSV('databases/pokedex.csv')

def main():
    """Ask user for input and call getBestCounter() to solve it"""
    while(True):
        defenderPkm = input('Opponent: ').strip().lower()

        start_time = time.time()
        for row in pokedexData:
            if row['Pokemon Name'].lower() == defenderPkm:
                getBestCounter(defenderPkm)
                print("--- %s seconds ---" % (time.time() - start_time))
                break
        else:
            print("Sorry we don't have that pokemon yet")
            print("--- %s seconds ---" % (time.time() - start_time))

        answer = input("Another one? y/n > ")
        while answer.strip().lower() not in ("y", "n"):
            answer = input("Another one? y/n > ")
        if answer.strip().lower() == "n":
            exit()


def getBestCounter(defenderPkm):
    """This function does the printing and calling core functions of the algorithm"""
    print('Pokemon Name: '+defenderPkm.capitalize())
    if defenderPkm == 'None':
        print('\n')
    else:
        result = compareAllDPS(findPKMToFight(defenderPkm), defenderPkm)
        for i in range(10):
            del result[i]['DPS']
            del result[i]['TDO']
            del result[i]['Damage']
            del result[i]['Type Adv']
            print(result[i])

main()

