import numpy as np
from NeuralNetwork.Neuron import Agent as agent


# Train

class Seleccion:

    def __init__(self):
        self.result = []
        self.data = np.loadtxt("iris.data", delimiter=',')
        self.featuresA = self.data[0:50, 0:-1]
        self.featuresB = self.data[50:100, 0:-1]
        self.featuresC = self.data[100:150, 0:-1]
        self.classes = [[0, 0], [0, 1], [1, 0]]
        self.N = agent(4, 3, 2, 0.2, 0.5)

    #def SetWeight(self, weight):


    def Seleccion(self):
        i = 0
        while i < 1000:
            j = 0
            while j < 50:
                O, H = self.N.calcNetOutput(list(self.featuresA[j]), True)
                self.N.trainingEpisode(self.classes[0], O, H, list(self.featuresA[j]))

                O, H = self.N.calcNetOutput(list(self.featuresB[j]), True)
                self.N.trainingEpisode(self.classes[1], O, H, list(self.featuresB[j]))

                O, H = self.N.calcNetOutput(list(self.featuresC[j]), True)
                self.N.trainingEpisode(self.classes[2], O, H, list(self.featuresC[j]))

                j += 1
            i += 1

        O = self.N.calcNetOutput(list(self.featuresA[0]), False)
        self.result.append(O)
        O = self.N.calcNetOutput(list(self.featuresB[0]), False)
        self.result.append(O)
        O = self.N.calcNetOutput(list(self.featuresC[0]), False)
        self.result.append(O)

    def GetResult(self):
        return self.result
