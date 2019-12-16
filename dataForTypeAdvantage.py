from dataFromPokedex import readCSV
'''This file looks up type advantage scores from type advantage database'''

typesData = readCSV('databases/types.csv')


def lookupTypeAdvantage(typeAttacker, typeDefender):
    '''Check type advantages'''
    for row in typesData:
        if row['Attack'].lower() == typeAttacker.lower():
            return float(row[typeDefender.capitalize()])
    return 0