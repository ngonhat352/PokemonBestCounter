from dataFromPokedex import readCSV
from bestPkmToChoose import findPKMToFight

dpsData = readCSV('databases/comprehensive_dps.csv')

def getDPS(pokemonName, fastMove, chargedMove):
    """Given a pokemon name, one of its fast moves and charged moves, get its DPS """
    for row in dpsData:
        if (pokemonName.lower() == row['Pokemon'].lower() and (fastMove == row['Fast Move'])
                and (chargedMove==row['Charged Move'])):
            return row['DPS']
    return 0

def getTDO(pokemonName, fastMove, chargedMove):
    """Given a pokemon name, one of its fast moves and charged moves, get its DPS """
    for row in dpsData:
        if (pokemonName.lower() == row['Pokemon'].lower() and (fastMove == row['Fast Move'])
                and (chargedMove==row['Charged Move'])):
            return row['TDO']
    return 0


