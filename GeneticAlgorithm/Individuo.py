import numpy as np
import random as rd


class individuo:

    def __init__(self, quantity, mutacionPercentage):
        self.calificacion = 0
        self.relacionMutua = 0
        self.mutacionProbability = mutacionPercentage
        self.genotipo = np.random.uniform(-30, 30, quantity)

    def newcomer(self, genotipo):
        self.genotipo = genotipo

    def Mutacion(self):
        i = rd.randint(len(self.genotipo))
        v = rd.gauss(0, 15)
        tmp = self.genotipo.copy()
        self.genotipo[i] = abs(self.genotipo[i] + v)
        print('El individuo {} muto a {}'.format(tmp, self.genotipo))
