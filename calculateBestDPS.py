from bestPkmToChoose import findPKMToFight
from bestTypeToChoose import calculateTypeAdvantage
from dataForDPS import getDPS, getTDO
from dataFromPokedex import getFastMoves, getChargedMoves, getTypesByPKM
from movesetTypes import getTypeOfFMove, getTypeOfCMove


def getAllDPS(pokemon):
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
            # combinations = sorted(combinations,key=lambda x: (x['DPS']),reverse=True)
    return combinations

def getAttackDPS(attacker, defender):
    """Given a pokemon and a defender, calculate all of its possible fast moves and charged moves combinations with its DPS,
    then sort those combinations from strongest to weakest"""
    movesets = getAllDPS(attacker)
    result = []
    for aMoveSet in movesets:
        #TODO: CHECK FORMULA BELOW ...when choosing move, prioritize the type! => currently not have that (mewtwo!) + haven't calculated resistance
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
    """Given a list of pokemon, return a list of best moves possible of those pokemon and sort them by strong to weak DPS"""
    allDPS=[]
    for pokemon in arrayOfPokemon:
        allDPS.append(getAttackDPS(pokemon,defender))

    result = []
    for i in allDPS:
        if i != [] :
            result.append(i[0])   #i[0] because we only care about the best moves combination for each pokemon

    result = sorted(result, key=lambda x: (x['Damage']), reverse=True)
    return result

# Cases that fail: Hydreigon,

