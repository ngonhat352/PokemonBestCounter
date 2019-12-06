from bestTypeToChoose import calculateTypeAdvantage
from dataFromPokedex import getFastMoves, getChargedMoves, readCSV
from findPokemonToFight import findPKMToFight
from movesetTypes import getTypeOfFMove, getTypeOfCMove

dpsData = readCSV('databases/comprehensive_dps.csv')

def getDPS(pokemonName, fastMove, chargedMove):
    """Given a pokemon name, one of its fast moves and charged moves, get its DPS """
    for row in dpsData:
        if (pokemonName.lower() == row['Pokemon'].lower() and (fastMove == row['Fast Move'])
                and (chargedMove==row['Charged Move'])):
            return row['DPS^3*TDO']
    return 0

###################### DPS calculations and sortings ####################################

def getAllDPS(attacker, defender):
    """Given a pokemon, give all of its possible fast moves and charged moves combinations with its DPS,
    then sort those combinations from strongest to weakest"""
    combinations = []
    fastMoves = getFastMoves(attacker)
    chargedMoves = getChargedMoves(attacker)
    if fastMoves == "Sorry we don't have that Gen yet D:":
        return "Sorry we don't have that Gen yet D:"
    for f in fastMoves:
        for c in chargedMoves:
            if f == '' or c == '':
                break
            oneDPS = {}
            oneDPS['Pokemon:'] = attacker
            oneDPS['Fast Move']=f
            oneDPS['Charged Move']=c

            #TODO: lost priority of type!
            oneDPS['DPS'] = float(getDPS(attacker, f, c)) \
            * (calculateTypeAdvantage(getTypeOfFMove(f), defender) + calculateTypeAdvantage(getTypeOfCMove(c),defender))

            combinations.append(oneDPS)
            # if float(getDPS(pokemonName, f, c))==0:
            #     print(pokemonName,f,c)
        combinations = sorted(combinations,key=lambda x: (x['DPS']),reverse=True)
    return combinations

def compareAllDPS(arrayOfPokemon,defender):
    """Given a list of pokemon, return a list of best moves possible of those pokemon and sort them by strong to weak DPS"""
    allDPS=[]
    for pokemon in arrayOfPokemon:
        allDPS.append(getAllDPS(pokemon,defender))

    result = []
    for i in allDPS:
        if i != []:
            result.append(i[0])   #i[0] because we only care about the best moves combination for each pokemon

    result = sorted(result, key=lambda x: (x['DPS']), reverse=True)
    return result

for i in compareAllDPS(findPKMToFight('Emboar'),'Emboar'):
    print(i)