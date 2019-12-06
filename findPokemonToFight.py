from dataFromPokedex import readCSV
from bestTypeToChoose import best3TypesToChoose
from movesetTypes import getFMovesOfType, getCMovesOfType

pokedex = readCSV('databases/pokedex.csv')

def getPKMofFMove(fmove):
    """Get all the pokemon that have that fast moveset"""
    result = []
    for row in pokedex:
        if row['fmove1'] == fmove or row['fmove2'] == fmove or row['fmove3'] == fmove \
        or row['fmove4'] == fmove or row['fmove5'] == fmove or row['fmove6'] == fmove or row['fmove7'] == fmove:
            result.append(row['Pokemon Name'])
    return result

def getPKMofCMove(cmove):
    """Get all the pokemon that have that charged moveset"""
    result = []
    for row in pokedex:
        if row['cmove1'] == cmove or row['cmove2'] == cmove or row['cmove3'] == cmove or row['cmove4'] == cmove \
        or row['cmove5'] == cmove or row['cmove6'] == cmove or row['cmove7'] == cmove or row['cmove8'] == cmove:
            pokemon = row['Pokemon Name']
            if pokemon not in result:
                result.append(pokemon)
    return result

def findPKMToFight(pokemon):
    top3Types=best3TypesToChoose(pokemon)
    fMovesList = []
    cMovesList = []
    pokemonList = []

    for i in range(3):
        aType = top3Types[i]['Type']
        fMovesList = fMovesList + getFMovesOfType(aType)
        cMovesList = cMovesList + getCMovesOfType(aType)

    for fmove in fMovesList:
        pokemonList = pokemonList + getPKMofFMove(fmove)

    for cmove in cMovesList:
        pokemonList = pokemonList + getPKMofCMove(cmove)

    pokemonList.sort()
    #TODO: remove duplicates

    return pokemonList


findPKMToFight('Moltres')



