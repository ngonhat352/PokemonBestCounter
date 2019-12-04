import csv
from decimal import Decimal

def readCSV(csvFilename):
    """This is a function to read in and return data from a CSV file
    as a list of dictionaries.  It does *not* convert the numeric
    values to integers"""
    fileObj = open(csvFilename, 'r')
    myReader = csv.DictReader(fileObj)
    # initialize table to be empty
    table = []
    for row in myReader:
        table.append(row)
    fileObj.close()
    return table

def getTypes(pokemonName, data):
    """Given a pokemon name, get its type. BUT: put 'Diglett (Alolan)'
    if it is the alolan form AND 'Castform (Ice)' if it has multiple forms and elements"""
    for row in data:
        if pokemonName.lower() == row['Pokemon Name'].lower():
            if row['Type 2'] != '':
                return [row['Type 1'],row['Type 2']]
            else:
                return [row['Type 1']]
    return "Sorry we don't have that Gen yet D:"

def getFastMoves(pokemonName, data):
    """Given a pokemon name, get its possible fast move"""
    for row in data:
        if pokemonName.lower() == row['Pokemon Name'].lower():
            return row['fmove1'],row['fmove2'],row['fmove3'],row['fmove4'],row['fmove5'],row['fmove6'],row['fmove7']
    return "Sorry we don't have that Gen yet D:"

def getChargedMoves(pokemonName, data):
    """Given a pokemon name, get its possible fast move"""
    for row in data:
        if pokemonName.lower() == row['Pokemon Name'].lower():
            return row['cmove1'],row['cmove2'],row['cmove3'],row['cmove4'],row['cmove5'],\
                   row['cmove6'],row['cmove7'],row['cmove8']

    return "Sorry we don't have that Gen yet D:"

def getDPS(pokemonName, fastMove, chargedMove, data):
    """Given the pokemon name, fast move and charged move, get its DPS """
    for row in data:
        if (pokemonName.lower() == row['Pokemon'].lower() and (fastMove == row['Fast Move'])
                and (chargedMove==row['Charged Move'])):
            return row['DPS^3*TDO']
    return 0

def getAllDPS(pokemonName, pokemonData, dpsData):
    """Given a pokemon, give all of its possible fast moves and charged moves combinations with its DPS,
    then sort those combinations from strongest to weakest"""
    combinations = []
    fastMoves = getFastMoves(pokemonName, pokemonData)
    chargedMoves = getChargedMoves(pokemonName, pokemonData)
    if fastMoves == "Sorry we don't have that Gen yet D:":
        return "Sorry we don't have that Gen yet D:"
    for f in fastMoves:
        for c in chargedMoves:
            if f == '' or c == '':
                break
            oneDPS = {}
            oneDPS['Pokemon:'] = pokemonName
            oneDPS['Fast Move']=f
            oneDPS['Charged Move']=c
            oneDPS['DPS'] = float(getDPS(pokemonName, f, c, dpsData)) # nhân cho typeAdvantage() (1 nếu ko có, 2 nếu có, 1/2 nếu bị resisted)
            combinations.append(oneDPS)
            # if float(getDPS(pokemonName, f, c))==0:
            #     print(pokemonName,f,c)
        combinations.sort(reverse=True,key=functionForSortByDPS)

    return combinations

def functionForSortByDPS(list):
    return list['DPS']

def compareAllDPS(arrayOfPokemon,pokemonData, dpsData):
    a=[]
    for pokemon in arrayOfPokemon:
        a.append(getAllDPS(pokemon,pokemonData,dpsData))

    result = []
    for i in a:
        result.append(i[0]) #get the strongest combination for each pokemon!
    result.sort(reverse=True,key=functionForSortByDPS)

    return result


# for i in compareAllDPS(['Mewtwo','Machamp','Groudon']):
#     print(i)

print(getTypes('snivy',readCSV('pokedex.csv')))