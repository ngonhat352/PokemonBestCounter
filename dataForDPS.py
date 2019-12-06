from bestTypeToChoose import calculateTypeAdvantage
from dataFromPokedex import getFastMoves, getChargedMoves, readCSV, getTypesByPKM
from findPokemonToFight import findPKMToFight
from movesetTypes import getTypeOfFMove, getTypeOfCMove

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
###################### DPS calculations and sortings ####################################
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
            oneDPS = {}
            oneDPS['Pokemon:'] = pokemon
            oneDPS['Fast Move'] = f
            oneDPS['Charged Move'] = c
            oneDPS['DPS'] = (float(getDPS(pokemon, f, c))**3)*float(getTDO(pokemon,f,c))
            combinations.append(oneDPS)
            combinations = sorted(combinations,key=lambda x: (x['DPS']),reverse=True)
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
        typeAdvantage = (calculateTypeAdvantage(typeF, defender) + calculateTypeAdvantage(typeC, defender))/2
        stabCount = 0
        stab = 1
        if typeF in getTypesByPKM(attacker):
            stabCount =stabCount+1
        if typeC in getTypesByPKM(attacker):
            stabCount =stabCount+1
        if stabCount==2:
            stab=1.5
        if stabCount==1:
            stab=1.25
        aMoveSet['DPS'] = (stab) *((float(getDPS(attacker, f, c)) *typeAdvantage)**3) * (float(getTDO(attacker,f,c))*typeAdvantage)
        aMoveSet['Type Adv'] = typeAdvantage
        result.append(aMoveSet)

    result = sorted(result,key=lambda x: (x['DPS']),reverse=True)
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

    result = sorted(result, key=lambda x: (x['DPS']), reverse=True)
    return result
# Cases that fail: Hydreigon,
for i in compareAllDPS(findPKMToFight('Metagross'),'Metagross'):
    print(i)