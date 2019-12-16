from dataFromPokedex import readCSV
from bestTypeToChoose import best3TypesToChoose
from movesetTypes import getFMovesOfType, getCMovesOfType
'''This file will be used for the 2nd and 3rd steps. It has functions to get the Pokemon 
that have the fast moves and charged moves of the desired type. 
Those are the desired Pokemon that will be used to put in compareAllDPS() '''


pokedex = readCSV('databases/comprehensive_dps.csv')

def getPKMofFMove(fmove):
    """Get all the pokemon that have that fast moveset"""
    result = []
    for row in pokedex:
        if row['Fast Move'] == fmove:
            result.append(row['Pokemon'])
    return result

def getPKMofCMove(cmove):
    """Get all the pokemon that have that charged moveset"""
    result = []
    for row in pokedex:
        if row['Charged Move'] == cmove:
            pokemon = row['Pokemon']
            if pokemon not in result:
                result.append(pokemon)
    return result

def findPKMToFight(pokemon):
    """After .........................."""
    top3Types=best3TypesToChoose(pokemon)
    fMovesList = []
    cMovesList = []
    pokemonList = []
    fmovePkm = []
    cmovePkm = []

    for i in top3Types:
        desiredType = i['Type']
        fMovesList = fMovesList + getFMovesOfType(desiredType)
        cMovesList = cMovesList + getCMovesOfType(desiredType)

    for fmove in fMovesList:
        fmovePkm = fmovePkm + getPKMofFMove(fmove)

    for cmove in cMovesList:
        cmovePkm =  cmovePkm+getPKMofCMove(cmove)

    for i in fmovePkm:
        if i not in pokemonList:
            pokemonList.append(i)

    for i in cmovePkm:
        if i not in pokemonList:
            pokemonList.append(i)

    # pokemonList.sort()
    return pokemonList



