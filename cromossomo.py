class Cromossomo:

  def __init__(self, config):
    self.config = config

  def __str__(self):
    to_string = 'Inteiro: ' + str(self.config['inteiro']) + ': ' + 'Binario: '+str(self.config['binario']) + ','
    return to_string + '\n'