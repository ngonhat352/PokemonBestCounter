from bestTypeToChoose import calculateTypeAdvantage
from dataForDPS import getDPS, getTDO
from dataFromPokedex import getFastMoves, getChargedMoves, getTypesByPKM
from movesetTypes import getTypeOfFMove, getTypeOfCMove
'''This file is the last step of our algorithm.
It has functions to calculate DPS and TDO of a Pokemon by itself and against an opponent'''


def getAllDPS(pokemon):
    """Given a pokemon, calculate all of its possible fast moves and charged moves combinations
    with its DPS, then sort those combinations from strongest to weakest"""
    combinations = []
    fastMoves = getFastMoves(pokemon)
    chargedMoves = getChargedMoves(pokemon)
    if fastMoves == "Sorry we don't have that Gen yet D:":
        return "Sorry we don't have that Gen yet D:"
    for f in fastMoves:
        for c in chargedMoves:
            if f == '' or c == '':
                break
            aMoveSet = {}
            aMoveSet['Pokemon:'] = pokemon
            aMoveSet['Fast Move'] = f
            aMoveSet['Charged Move'] = c
            aMoveSet['DPS'] = float(getDPS(pokemon, f, c))
            aMoveSet['TDO'] = float(getTDO(pokemon,f,c))
            combinations.append(aMoveSet)
    return combinations

def getAttackDPS(attacker, defender):
    """Get all the movesets of the attacker Pokemon,
    then calculate their damage with type advantage against the defender Pokemon"""
    movesets = getAllDPS(attacker)
    result = []
    for aMoveSet in movesets:
        f = aMoveSet['Fast Move']
        c = aMoveSet['Charged Move']
        typeF = getTypeOfFMove(f)
        typeC = getTypeOfCMove(c)
        typeAttacker = getTypesByPKM(attacker)
        typeAdvantage = (calculateTypeAdvantage(typeF, defender) + calculateTypeAdvantage(typeC, defender)*2)/3
        stab = 1
        if typeF in typeAttacker and typeC in typeAttacker:
            stab = 1.5
        if typeC in typeAttacker or typeF in typeAttacker:
            stab=1.25
        aMoveSet['Damage'] = (stab) *((aMoveSet['DPS'] *typeAdvantage)**3) * (aMoveSet['TDO']*typeAdvantage)
        aMoveSet['Type Adv'] = typeAdvantage
        result.append(aMoveSet)

    result = sorted(result,key=lambda x: (x['Damage']),reverse=True)
    return result

def compareAllDPS(arrayOfPokemon,defender):
    """Given a list of pokemon, calculate the DPS against the defender pokemon
    and then return a list of best moves possible of those pokemon."""
    allDPS=[]
    for pokemon in arrayOfPokemon:
        allDPS.append(getAttackDPS(pokemon,defender))

    result = []
    for i in allDPS:
        if i != []:
            result.append(i[0])   #i[0] because we only care about the best moves combination for each pokemon

    result = sorted(result, key=lambda x: (x['Damage']), reverse=True)

    return result



