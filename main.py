from bestPkmToChoose import findPKMToFight
from calculateBestDPS import compareAllDPS
import time
from dataFromPokedex import readCSV

pokedexData = readCSV('databases/pokedex.csv')

def main():
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
    print('Pokemon Name: '+defenderPkm.capitalize())
    if defenderPkm == 'None':
        print('\n')
    else:
        result = compareAllDPS(findPKMToFight(defenderPkm), defenderPkm)
        for i in range(10):
            print(result[i])

main()

