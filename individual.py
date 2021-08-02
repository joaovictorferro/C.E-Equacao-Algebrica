from random import randint, seed
from datetime import datetime
import numpy as np
from cromossomo import Cromossomo

class Individual:

  def __init__(self,cromossomo = None):
    if cromossomo is None:
      self.cromossomo = []
      for i in range(20):
        config = {
        }
        aleatorio = np.random.randint(-13000, 13000)
        config['inteiro'] = aleatorio
        config['binario'] = bin(aleatorio)
        config['score'] = 100000
        cromossomo = Cromossomo(config)
        self.cromossomo.append(cromossomo)
    else:
      self.cromossomo = cromossomo

  def __str__(self) :
    cromossomo = ''
    for i in range(len(self.cromossomo)):
      cromossomo += str(self.cromossomo[i])
    return cromossomo + '\n'