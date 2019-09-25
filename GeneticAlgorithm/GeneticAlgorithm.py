from GeneticAlgorithm.Individuo import individuo
from NeuralNetwork.Seleccion import Seleccion

import numpy as np


class geneticAlgorithm:

    def __init__(self, gentiCodeLen, population, mutacionPercentage, elitism, geneticMerch, percentageNewcomers,
                 generaciones):
        self.poblacion = []
        self.herederos = []
        self.GenerarPoblacion(gentiCodeLen, population, mutacionPercentage)
        for i in range(generaciones):
            print("<---------------------------------------------------------------------------------------->")
            print('Generacion {}'.format(i))
            print()
            for ind in self.poblacion:
                print(ind.genotipo)
            print()
            self.Seleccion()
            print()
            while len(self.herederos) < (len(self.poblacion) * percentageNewcomers):
                indA = self.poblacion[np.random.randint(0, len(self.poblacion) - 1)]
                indB = self.poblacion[np.random.randint(0, len(self.poblacion) - 1)]
                self.Cruzar(indA, indB, geneticMerch)
            print()
            self.Reinsertion(elitism)
            print()
            self.Elite()
            print()
            self.Mutar()

    def GenerarPoblacion(self, genotipo, cantidad, mutacionProbability):
        for i in range(cantidad):
            self.poblacion.append(individuo(genotipo, mutacionProbability))

    def Evaluacion(self):
        print("Evaluacion de individuos")
        neuron = Seleccion.__init__()
        for ind in self.poblacion:
            evaluacion = 0
            ind.calificacion = evaluacion
            print('Evaluacion del individuo {}, evaluacion = {}'.format(ind.genotipo, evaluacion))

    def Seleccion(self):
        print("<Seleccion de individuos>")
        total = 0
        self.Evaluacion()
        for ind in self.poblacion:
            total += ind.calificacion
        for ind in self.poblacion:
            rm = ind.calificacion / total
            ind.relacionMutua = rm
            print('Relacion Mutua del Individuo {} es = {}'.format(ind.genotipo, rm))

    def Mutar(self):
        for ind in self.poblacion:
            ind.Mutacion()

    def Cruzar(self, indA, indB, percentage):
        i = int(percentage * len(indA.genotipo))
        genA = indA.genotipo[:i]
        genB = indB.genotipo[i:]
        gen = np.concatenate((genA, genB), axis=0)
        new = individuo(len(indA.genotipo), indA.mutacionProbability)
        new.newcomer(gen)
        self.herederos.append(new)
        genA = indA.genotipo[i:]
        genB = indB.genotipo[:i]
        gen = np.concatenate((genB, genA), axis=0)
        new2 = individuo(len(indB.genotipo), indB.mutacionProbability)
        new2.newcomer(gen)
        self.herederos.append(new2)
        print('Nuevos individuos nacidos de {} y {}. Los individuos son {} y {}'.format(indA.genotipo, indB.genotipo,
                                                                                        new.genotipo, new2.genotipo))

    def Reinsertion(self, elit):
        print("Reinsercion")
        for i in range(int(elit * len(self.poblacion))):
            tmp = self.poblacion[0]
            for ind in self.poblacion:
                if tmp.relacionMutua < ind.relacionMutua:
                    tmp = ind
            self.herederos.append(tmp)
            self.poblacion.remove(tmp)
            print(
                'El individuo {} destaco de los demas con una relacion mutua de {}'.format(tmp.genotipo,
                                                                                           tmp.relacionMutua))
        self.poblacion.clear()
        for ind in self.herederos:
            self.poblacion.append(ind)
        self.herederos.clear()

    def Elite(self):
        self.elit = self.poblacion[0]
        for ind in self.poblacion:
            if self.elit.relacionMutua < ind.relacionMutua:
                self.elit = ind
        print('Individuo con mejor resultado fue {} con calificacion de {}'.format(self.elit.genotipo,
                                                                                   self.elit.calificacion))

    def getElit(self):
        return self.elit