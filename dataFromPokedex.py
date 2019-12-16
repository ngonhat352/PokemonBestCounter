import csv
"""Nathan Ngo, Alejandro Aguilar, Saby Cortez

This file has functions to extract the most basic data (types of the pokemon, its moves) 
from the pokedex database and the dps database"""


def readCSV(csvFilename):
    """This is a function from COMP 123 to read in and return data from a CSV file
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
dpsData = readCSV('databases/comprehensive_dps.csv')

def getTypesByPKM(pokemonName):
    """Given a pokemon name, get its type. BUT: put 'Diglett (Alolan)'
    if it is the alolan form AND 'Castform (Ice)' if it has multiple forms and elements"""
    for row in pokedexData:
        if pokemonName.lower() == row['Pokemon Name'].lower():
            if row['Type 2'] != '':
                return [row['Type 1'],row['Type 2']]
            else:
                return [row['Type 1']]
    return []

def getFastMoves(pokemonName):
    """Given a pokemon name, get all of its possible fast moves"""
    result = []
    for row in dpsData:
        if pokemonName.lower() == row['Pokemon'].lower():
            if row['Fast Move'] not in result:
                result.append(row['Fast Move'])
    return result

def getChargedMoves(pokemonName):
    """Given a pokemon name, get its possible charged moves"""
    result = []
    for row in dpsData:
        if pokemonName.lower() == row['Pokemon'].lower():
            if row['Charged Move'] not in result:
                result.append(row['Charged Move'])
    return result

def getPkmByTypes(type1,type2=''):
    """Given the types, get a pokemon that has that type! Type 2 by default is blank - one-type Pokemon.
    Used for testing"""
    for row in pokedexData:
        if ((row['Type 1'] == type1 and row['Type 2'] == type2)
        or (row['Type 1'] == type2 and row['Type 2'] == type1)):
            if ('(' not in row['Pokemon Name']):
                return row['Pokemon Name']
    return 'None'

# print(getTypesByPKM(getPkmByTypes('Normal')))
# print(getPkmByTypes('Normal','Normal'))
