import csv

from datasearch import readCSV,compareAllDPS

pokedexData = readCSV('pokedex.csv')
dpsData = readCSV('comprehensive_dps.csv')

def top10ofAll(pokemonData, dpsData):
    allPokemon = []
    for row in pokemonData:
        allPokemon.append(row['Pokemon Name'])

    dpsList = compareAllDPS(allPokemon,pokemonData,dpsData)
    result = []
    for i in range(10):
        result.append(dpsList[i])
    return result

def top10ofType(type, pokemonData, dpsData):
    allPokemonOfType = []
    for row in pokemonData:
        if row['Type 1'] == type or row['Type 2']==type:
            allPokemonOfType.append(row['Pokemon Name'])

    dpsList = compareAllDPS(allPokemonOfType,pokemonData,dpsData)
    result = []
    for i in range(10):
        result.append(dpsList[i])
    return result


# top10ofAll = top10ofAll(pokedexData,dpsData)
# top10ofFire = top10ofType('Fire',pokedexData,dpsData)
top10ofRock = top10ofType('Rock',pokedexData,dpsData)


for i in top10ofRock:
    print(i)
