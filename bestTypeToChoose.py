from dataForTypeAdvantage import lookupTypeAdvantage
from dataFromPokedex import getTypesByPKM



listOfTypes = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire',
               'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison',
               'Psychic', 'Rock', 'Steel', 'Water']


def calculateTypeAdvantage(attackType, defensePKM):
    """How effective a type is towards a pokemon when the type attacks"""
    typesOfDefensePKM = getTypesByPKM(defensePKM)  # intrinsic type of the defense pokemon
    typeAdvantage = 1
    # attackType attacking the defense pkm
    for i in typesOfDefensePKM:
        typeAdvantage = typeAdvantage * lookupTypeAdvantage(attackType, i)

    return typeAdvantage

def calculateAdvDefendingToPKM(type, pokemon):
    typesOfDefenseFMoves = getTypesOfAllFMoves(pokemon)
    typesOfDefenseCMoves = getTypesOfAllCMoves(pokemon)
    score = 0

    # Type defending from the movesets of the pkm
    for i in typesOfDefenseFMoves:
        if (lookupTypeAdvantage(i[0], type) > 1):
            score = score - 1
            # print('Strong against the type:' + i[1])
        elif (lookupTypeAdvantage(i[0], type) < 1):
            score = score + 1
            # print('Weak against the type:' + i[1])
        else:
            pass

    for i in typesOfDefenseCMoves:
        if (lookupTypeAdvantage(i[0], type) > 1):
            score = score - 1
            # print('Strong against the type:' + i[1])

        elif (lookupTypeAdvantage(i[0], type) < 1):
            score = score + 1
            # print('Weak against the type:' + i[1])
        else:
            pass

    return score


def bestTypesToChoose(pokemon):
    """Return the best 5 types to attack the input pokemon"""
    result = []
    for i in listOfTypes:
        result.append({'Type': i, 'Type Advantage': calculateTypeAdvantage(i, pokemon),
                       'Score': calculateAdvDefendingToPKM(i,pokemon)})

    result = sorted(result, key=lambda x: (x['Type Advantage'], x['Score']), reverse=True)
    # prioritize typeAdvantage, then if equal, rank according to score
    # TODO: THEN MULTIPLY TYPE ADVANTAGE TO DPS => WHERE??

    return [result[0],result[1],result[2],result[3],result[4]]  #Top 5 types


print(bestTypesToChoose('Poliwrath'))



# def calculateTypeAdvantage(attackPKM,defensePKM,pokedex,typesData, fmoveData, cmoveData):
#     typesOfAttackPKM = getTypesByPKM(attackPKM,pokedex) #intrinsic type of the attack pokemon
#     typesOfDefensePKM = getTypesByPKM(defensePKM,pokedex) #intrinsic type of the defense pokemon
#
#     typesOfAttackFMoves = getTypesOfAllCMoves(attackPKM,pokedex,fmoveData) #types of all the fast moves of the attack pokemon
#     typesOfAttackCMoves = getTypesOfAllCMoves(attackPKM,pokedex,cmoveData) #types of all the charged moves of the attack pokemon
#
#     typesOfDefenseFMoves = getTypesOfAllFMoves(defensePKM,pokedex,fmoveData)
#     typesOfDefenseCMoves = getTypesOfAllCMoves(defensePKM,pokedex,cmoveData)
#
#     result = 1
#
#     for i in typesOfAttackPKM:
#         for j in typesOfDefensePKM:
#             result = result* lookupTypeAdvantage(i,j,typesData)
#             print("Attack type: "+i+", Defense Type: "+j+", type advantage: "+str(result))
#
#     for i in typesOfDefensePKM:
#         for j in typesOfAttackPKM:
#             result = result/ lookupTypeAdvantage(i,j,typesData)
#             print("Attack type: "+i+", Defense Type: "+j+", type advantage: "+str(result))
#     return result
# print(calculateTypeAdvantage('Gengar','Snorlax',readCSV('pokedex.csv'),readCSV('types.csv')))