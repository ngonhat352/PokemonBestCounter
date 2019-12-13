from bestPkmToChoose import findPKMToFight
from calculateBestDPS import compareAllDPS
import time


while(True):

    defenderPkm = input('Opponent: ').capitalize()
    start_time = time.time()
    result = compareAllDPS(findPKMToFight(defenderPkm), defenderPkm)
    for i in range(10):
        print(result[i])
    print("--- %s seconds ---" % (time.time() - start_time))

# Hydreigon has MEW? We lost Terrakion /


