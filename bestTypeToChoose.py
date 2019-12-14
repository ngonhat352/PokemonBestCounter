from dataForTypeAdvantage import lookupTypeAdvantage
from dataFromPokedex import getTypesByPKM
from movesetTypes import getTypesOfAllFMoves, getTypesOfAllCMoves

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


def best3TypesToChoose(pokemon):
    """Return the best 3 types to attack the input pokemon"""
    result = []
    for i in listOfTypes:
        result.append({'Type': i, 'Type Advantage': calculateTypeAdvantage(i, pokemon),
                       'Score': calculateAdvDefendingToPKM(i,pokemon)})

    result = sorted(result, key=lambda x: (x['Type Advantage'], x['Score']), reverse=True)
    # prioritize typeAdvantage, then if equal, rank according to score

    return [result[0],result[1],result[2]]  #Top 3 types

