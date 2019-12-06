from dataFromPokedex import readCSV, getChargedMoves, getFastMoves

fmovesData = readCSV('databases/movesquick.csv')
cmovesData = readCSV('databases/movescharge.csv')

def getTypeOfFMove(fmove):
    """Given the name of a fast move, return the type of that move. """
    for row in fmovesData:
        if row['ï»¿Quick Move'] == fmove:
            return row['Type']
    return "Not a valid move"


def getTypeOfCMove(cmove):
    """Given the name of a charged move, return the type of that move. """
    for row in cmovesData:
        if row['ï»¿Charge Move'] == cmove:
            return row['Type']
    return "Not a valid move"


def getTypesOfAllFMoves(pokemon):
    """Given a pokemon, get the types of all of its fast moves"""
    allFMoves = getFastMoves(pokemon)

    result = []
    for oneMove in allFMoves:
        type = getTypeOfFMove(oneMove)
        if type != 'Not a valid move':
            result.append([type, oneMove])
    return result


def getTypesOfAllCMoves(pokemon):
    """Given a pokemon, get the types of all of its charged moves"""
    allCMoves = getChargedMoves(pokemon)

    result = []
    for oneMove in allCMoves:
        type = getTypeOfCMove(oneMove)
        if type != 'Not a valid move':
            result.append([type, oneMove])
    return result


def getFMovesOfType(type):
    result = []
    for row in fmovesData:
        if row['Type'] == type:
            result.append(row['ï»¿Quick Move'])
    return result


def getCMovesOfType(type):
    result = []
    for row in cmovesData:
        if row['Type'] == type:
            result.append(row['ï»¿Charge Move'])
    return result

