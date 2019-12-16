from dataFromPokedex import getPkmByTypes
from main import *
'''This file is for testing. It gets all the possible combinations of types 
and run to find the strongest opponent to the Pokemon having those types'''


listOfTypes = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire',
               'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison',
               'Psychic', 'Rock', 'Steel', 'Water']

for i in listOfTypes:
    for j in listOfTypes:
        if i == j:
            print('===== '+i+' ===== ')
            getBestCounter(getPkmByTypes(i))
        else:
            print('===== '+i+' and '+j+' ===== ')
            getBestCounter(getPkmByTypes(i,j))





