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

def getTypesByPKM(pokemonName, data):
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

###################### DPS calculations and sortings ####################################

def getDPS(pokemonName, fastMove, chargedMove, data):
    """Given a pokemon name, one of its fast moves and charged moves, get its DPS """
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
    """TO be used for array.sort() to sort the list of dictionaries by the value of key 'DPS' """
    return list['DPS']

def compareAllDPS(arrayOfPokemon,pokemonData, dpsData):
    """Given a list of pokemon, return a list of best moves possible of those pokemon and sort them by strong to weak DPS"""
    allDPS=[]
    for pokemon in arrayOfPokemon:
        allDPS.append(getAllDPS(pokemon,pokemonData,dpsData))

    result = []
    for i in allDPS:
        if i != []:
            result.append(i[0])   #i[0] because we only care about the best moves combination for each pokemon

    result.sort(reverse=True,key=functionForSortByDPS)
    return result

######################## Type advantages and disadvantages calculations############################
def getTypeOfFMove(fmove,data):
    """Given the name of a fast move, return the type of that move. Will use movesquick.csv"""
    for row in data:
        if row['ï»¿Quick Move'] == fmove:
            return row['Type']
    return "Not a valid move"

def getTypeOfCMove(cmove,data):
    """Given the name of a charged move, return the type of that move. Will use movescharge.csv"""
    for row in data:
        if row['ï»¿Charge Move'] == cmove:
            return row['Type']
    return "Not a valid move"

def getTypesOfAllFMoves(pokemon,pokedex,movesData):
    """Given a pokemon, get the types of all of its fast moves"""
    allFMoves = getFastMoves(pokemon,pokedex)

    result = []
    for oneMove in allFMoves:
        type = getTypeOfFMove(oneMove,movesData)
        if type != 'Not a valid move':
            result.append([type,oneMove])
    return result

def getTypesOfAllCMoves(pokemon,pokedex,movesData):
    """Given a pokemon, get the types of all of its charged moves"""
    allCMoves = getChargedMoves(pokemon,pokedex)

    result = []
    for oneMove in allCMoves:
        type = getTypeOfCMove(oneMove,movesData)
        if type != 'Not a valid move':
            result.append([type,oneMove])
    return result

def basicTypeAdvantage(typeAttacker, typeDefender, typedata):
    '''Check type advantages'''
    for row in typedata:
        if row['Attack'].lower() == typeAttacker.lower():
            return float(row[typeDefender.capitalize()])
    return "Type not valid"

def calculateTypeAdvantage(attackPKM,defensePKM,pokedex,typesData, fmoveData, cmoveData):
    typesOfAttackPKM = getTypesByPKM(attackPKM,pokedex) #intrinsic type of the attack pokemon
    typesOfDefensePKM = getTypesByPKM(defensePKM,pokedex) #intrinsic type of the defense pokemon

    typesOfAttackFMoves = getTypesOfAllCMoves(attackPKM,pokedex,fmoveData) #types of all the fast moves of the attack pokemon
    typesOfAttackCMoves = getTypesOfAllCMoves(attackPKM,pokedex,cmoveData) #types of all the charged moves of the attack pokemon

    typesOfDefenseFMoves = getTypesOfAllFMoves(defensePKM,pokedex,fmoveData)
    typesOfDefenseCMoves = getTypesOfAllCMoves(defensePKM,pokedex,cmoveData)

    result = 1

    for i in typesOfAttackPKM: #TODO: not loop through the intrinsic type of the attack pkm rn, but the types of its possible moves
        for j in typesOfDefensePKM:
            result = result* basicTypeAdvantage(i,j,typesData) #TODO: not multiply by 2 if doubly effective: *2.56
            print("Attack type: "+i+", Defense Type: "+j+", type advantage: "+str(result))

    for i in typesOfDefensePKM: #TODO: not loop through the intrinsic type of the defense pkm rn, but the types of its possible moves
        for j in typesOfAttackPKM:
            result = result/ basicTypeAdvantage(i,j,typesData)
            print("Attack type: "+i+", Defense Type: "+j+", type advantage: "+str(result))
    return result

# print(calculateTypeAdvantage('Gengar','Snorlax',readCSV('pokedex.csv'),readCSV('types.csv')))