from dataFromPokedex import getPkmByTypes
from main import *

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





