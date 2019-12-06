from dataForDPS import compareAllDPS
from dataFromPokedex import readCSV


pokedexData = readCSV('databases/pokedex.csv')
dpsData = readCSV('databases/comprehensive_dps.csv')

def top10ofAll():
    allPokemon = []
    for row in pokedexData:
        allPokemon.append(row['Pokemon Name'])

    dpsList = compareAllDPS(allPokemon)
    result = []
    for i in range(10):
        result.append(dpsList[i])
    return result

def top10ofType(type):
    allPokemonOfType = []
    for row in pokedexData:
        if row['Type 1'] == type or row['Type 2']==type:
            allPokemonOfType.append(row['Pokemon Name'])

    dpsList = compareAllDPS(allPokemonOfType)
    result = []
    for i in range(10):
        result.append(dpsList[i])
    return result


top10ofAll = top10ofAll()
# top10ofFire = top10ofType('Fire')
# top10ofRock = top10ofType('Rock')


for i in top10ofAll:
    print(i)
