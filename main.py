#   Equipe:
#       Arthur Savio
#       Guilherme Amaral
#       Joao Victor Ribeiro
#   Polinomio:
#       3X20 7X19 8X18 7X17 1X16 3X15 4X14 2X13 3X12 8X11 9X10 7X9 12X8 3X7 6X6 2X5 9X4 5X3 11X2  11X1  2
#       G      U   I    L    H    E    R    M     E   V    O     L   N   E   Y   M   O    T   A    A    M
#   IDE: VSCODE

from random import seed
from random import *
from individual import Individual
from datetime import datetime

population = []
newpopulation = []
coeficiente =[2,11,11,5,9,2,6,3,12,7,9,8,3,2,4,3,1,7,8,7,3]
score = 0

seed(100)

def score():
    for ind in population:
        # inteiro = int(ind.individual,2)
        # print(inteiro)

        cont = 0
        seq = 0
        inteiro = 0
        for i in coeficiente:
            if seq ==0:
                cont += i
            else:
                inteiro = int(ind.binary, 2)
                cont += (inteiro**seq) * i
                print(inteiro)
            seq += 1
            ind.score = cont
            print(cont)

def init_population():
  for i in range(20):
    aleatorio = randint(-13000,13000)
    individual = Individual(aleatorio)
    #print(individual.binary)
    population.append(individual)

init_population()
# for ind in population:
#     print(ind.individual)
score()