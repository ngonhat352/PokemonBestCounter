import csv


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

pokedexData = readCSV('databases/pokedex.csv')

def getTypesByPKM(pokemonName):
    """Given a pokemon name, get its type. BUT: put 'Diglett (Alolan)'
    if it is the alolan form AND 'Castform (Ice)' if it has multiple forms and elements"""
    for row in pokedexData:
        if pokemonName.lower() == row['Pokemon Name'].lower():
            if row['Type 2'] != '':
                return [row['Type 1'],row['Type 2']]
            else:
                return [row['Type 1']]
    return "Sorry we don't have that Gen yet D:"

def getFastMoves(pokemonName):
    """Given a pokemon name, get its possible fast move"""
    for row in pokedexData:
        if pokemonName.lower() == row['Pokemon Name'].lower():
            return row['fmove1'],row['fmove2'],row['fmove3'],row['fmove4'],row['fmove5'],row['fmove6'],row['fmove7']
    return "Sorry we don't have that Gen yet D:"

def getChargedMoves(pokemonName):
    """Given a pokemon name, get its possible fast move"""
    for row in pokedexData:
        if pokemonName.lower() == row['Pokemon Name'].lower():
            return row['cmove1'],row['cmove2'],row['cmove3'],row['cmove4'],row['cmove5'],\
                   row['cmove6'],row['cmove7'],row['cmove8']

    return "Sorry we don't have that Gen yet D:"