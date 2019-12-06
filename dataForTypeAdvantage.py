from dataFromPokedex import readCSV, getTypesByPKM, getChargedMoves, getFastMoves



######################## Type advantages and disadvantages calculations############################
typesData = readCSV('databases/types.csv')

def lookupTypeAdvantage(typeAttacker, typeDefender):
    '''Check type advantages'''
    for row in typesData:
        if row['Attack'].lower() == typeAttacker.lower():
            return float(row[typeDefender.capitalize()])
    return 0


# def typeAdvantage2PKM(attacker,defender):
#     typeAdvantage = 1
#     for i in getTypesByPKM(attacker):
#         for j in getTypesByPKM(defender):
#             typeAdvantage = typeAdvantage* lookupTypeAdvantage(i, j)
#
#     for j in getTypesByPKM(defender):
#         for i in getTypesByPKM(attacker):
#             typeAdvantage = typeAdvantage / lookupTypeAdvantage(i, j)
#     return typeAdvantage