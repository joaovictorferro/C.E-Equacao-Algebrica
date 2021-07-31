from random import randint, seed
from datetime import datetime

class Individual:

  def __init__(self, individual):
    self.score = 10000000
    self.binary = bin(individual)
    # print(self.binary)

  def __str__(self) :
    return str(self.binary)