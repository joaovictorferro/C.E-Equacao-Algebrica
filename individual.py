from random import randint, seed
from datetime import datetime
import numpy as np
from cromossomo import Cromossomo

class Individual:

  def __init__(self,inteiro):
    self.score = 10000000
    self.binary = bin(inteiro)

  def __str__(self) :
    return str(self.binary)