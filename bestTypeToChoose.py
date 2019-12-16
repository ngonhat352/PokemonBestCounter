from dataForTypeAdvantage import lookupTypeAdvantage
from dataFromPokedex import getTypesByPKM
from movesetTypes import getTypesOfAllFMoves, getTypesOfAllCMoves
'''This file is used for the first step of the algorithm. Given an input pokemon, 
return the 3 types strongest against it by calculating type advantage and defense score'''



listOfTypes = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire',
               'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison',
               'Psychic', 'Rock', 'Steel', 'Water']

def calculateTypeAdvantage(attackType, defensePKM):
    """How effective a type is towards the input pokemon when the type attacks"""
    typesOfDefensePKM = getTypesByPKM(defensePKM)  # intrinsic type of the defense pokemon
    typeAdvantage = 1
    # attackType attacking the defense pkm
    for i in typesOfDefensePKM:
        typeAdvantage = typeAdvantage * lookupTypeAdvantage(attackType, i)
    return typeAdvantage

def calculateAdvDefendingToPKM(type, pokemon):
    """How resistant a type is when the input pokemon attacks
    - taking into account the type of the Pokemon's movesets"""
    typesOfFMoves = getTypesOfAllFMoves(pokemon)
    typesOfCMoves = getTypesOfAllCMoves(pokemon)
    score = 0

    # Type defending from the movesets of the pkm
    for i in typesOfFMoves:
        if (lookupTypeAdvantage(i[0], type) > 1):
            score = score - 1
            # The input pokemon's moveset has type advantage over the type we are measuring effectiveness
            # => it is not resistant against the defending Pokemon
        elif (lookupTypeAdvantage(i[0], type) < 1):
            score = score + 1
            # The type we are considering resists the moveset => Good to use
        else:
            pass
            # When type advantage is 1 => no special effect

    for i in typesOfCMoves:
        if (lookupTypeAdvantage(i[0], type) > 1):
            score = score - 1
        elif (lookupTypeAdvantage(i[0], type) < 1):
            score = score + 1
        else:
            pass

    return score


def best3TypesToChoose(pokemon):
    """Return the best 3 types to fight against the input pokemon,
    taking into account type advantage and defense score"""
    result = []
    for i in listOfTypes:
        result.append({'Type': i, 'Type Advantage': calculateTypeAdvantage(i, pokemon),
                       'Score': calculateAdvDefendingToPKM(i,pokemon)})

    result = sorted(result, key=lambda x: (x['Type Advantage'], x['Score']), reverse=True)
    # prioritize typeAdvantage, then if equal, rank according to score

    return [result[0],result[1],result[2]]  #Top 3 types

