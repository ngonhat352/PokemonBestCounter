from dataFromPokedex import readCSV



######################## Type advantages and disadvantages calculations############################
typesData = readCSV('databases/types.csv')

def lookupTypeAdvantage(typeAttacker, typeDefender):
    '''Check type advantages'''
    for row in typesData:
        if row['Attack'].lower() == typeAttacker.lower():
            return float(row[typeDefender.capitalize()])
    return 0