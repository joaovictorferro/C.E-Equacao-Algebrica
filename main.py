#   Equipe:
#       Arthur Savio
#       Guilherme Amaral
#       Joao Victor Ribeiro
#   Polinomio:
#       3X20 7X19 8X18 7X17 1X16 3X15 4X14 2X13 3X12 8X11 9X10 7X9 12X8 3X7 6X6 2X5 9X4 5X3 11X2  11X1  2
#       G      U   I    L    H    E    R    M     E   V    O     L   N   E   Y   M   O    T   A    A    M
#   IDE: VSCODE

import numpy as np
from individual import Individual
from datetime import datetime

population = []
roullete = []
newpopulation = []
coeficiente =[2,11,11,5,9,2,6,3,12,7,9,8,3,2,4,3,1,7,8,7,3]
score = 0


def list_as_roulette(soma_total):
    print("ENTREI AQUI")
    for ind in population:
        prop = round((ind.score*100)/soma_total)
        for j in range(prop):
            roullete.append(ind)
    print(len(roullete))

def score():
    for i in range(len(population)):
        cromossomo = population[i].cromossomo
        #print(cromossomo)
        for j in range(len(cromossomo)):
            cont = 0
            seq = 0
            inteiro = 0
            config = cromossomo[j].config
            for coe in coeficiente:
                if seq ==0:
                    cont += coe
                else:
                    inteiro = config['inteiro']
                    cont += (inteiro**seq) * coe
                    #print(inteiro)
                seq += 1
            config['score'] = cont
            print(cont)

def init_population():
  for i in range(1):
    individual = Individual()
    population.append(individual)

init_population()
for ind in population:
    print(ind)
score()
#
# soma_total = 0
# for ind in population:
#     soma_total+= ind.score
# list_as_roulette(soma_total)
# s = []
# for m in range(20):
#     r = np.random.randint(0,len(roullete)-1)
#     s = roullete[r]
#     print(s)