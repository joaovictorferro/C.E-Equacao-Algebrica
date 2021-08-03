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
raizes = []
newpopulation = []
coeficiente =[2,11,11,5,9,2,6,3,12,7,9,8,3,2,4,3,1,7,8,7,3]

def selection():
    qualquerLista = population + newpopulation
    qualquerLista = sorted(qualquerLista, key=lambda ind: abs(ind.score), reverse=True)
    selected_population = []
    for i in range(20):
        selected_population.append(qualquerLista[i])
    return selected_population

def mutation():
    population_mutation = 2
    for i in range(population_mutation):
        if len(newpopulation) != 0:
            ind_index = np.random.randint(0, len(newpopulation) - 1)
            individual = newpopulation[ind_index]
            pos = np.random.randint(3,20)
            if individual.binary[pos] == 0:
                individual.binary = individual.binary[:pos-1] + "1" + individual.binary[pos+1:]
            else:
                individual.binary = individual.binary[:pos - 1] + "0" + individual.binary[pos + 1:]


def cruzamentoParte2(pai,mae):
    part1 = np.random.randint(3,20)
    individuo1 = Individual(int(pai.binary[:part1] + mae.binary[part1:],2))
    individuo2 = Individual(int(mae.binary[:part1] + pai.binary[part1:],2))
    newpopulation.append(individuo1)
    newpopulation.append(individuo2)

def cruzamentoParte1():
    for i in range(10):
        aleatorio1 = np.random.randint(0,len(roullete)-1)
        aleatorio2 = np.random.randint(0,len(roullete)-1)
        while aleatorio1 == aleatorio2:
            aleatorio1 = np.random.randint(0, 100)
            aleatorio2 = np.random.randint(0, 100)

        pai = roullete[aleatorio1]
        mae = roullete[aleatorio2]
        cruzamentoParte2(pai, mae)

def list_as_roulette(soma_total):
    #print("ENTREI AQUI")
    for ind in population:
        prop = round((ind.score*100)/soma_total)
        for j in range(prop):
            roullete.append(ind)
    #print(len(roullete))

def score(population):
    for i in range(len(population)):
        cont = 0
        seq = 0
        inteiro = 0
        for coe in coeficiente:
            if seq ==0:
                cont += coe
            else:
                inteiro = int(population[i].binary,2)
                cont += (inteiro**seq) * coe
                #print(inteiro)
            seq += 1
        population[i].score = cont
        if cont == 0 and population[i].binary not in raizes:
            raizes.append(population[i].binary)
            ind_aleatorio = np.random.randint(-1000000,0)
            population[i].binary = bin(ind_aleatorio)
            cont = 0
            seq = 0
            for coe in coeficiente:
                if seq == 0:
                    cont += coe
                else:
                    inteiro = int(population[i].binary, 2)
                    cont += (inteiro ** seq) * coe
                    # print(inteiro)
                seq += 1
            population[i].score = cont
        #print(cont)

def init_population():
  for i in range(20):
    aleatorio = np.random.randint(-1000000,0)
    individual = Individual(aleatorio)
    population.append(individual)

init_population()
while True:
    for ind in raizes:
        print(ind)
    if len(raizes) == 20:
        break
    score(population)
    soma_total = 0
    for ind in population:
        soma_total+= ind.score
    list_as_roulette(soma_total)
    media = soma_total / 20
    cruzamentoParte1()
    mutation()
    score(newpopulation)
    population = selection()
    newpopulation.clear()