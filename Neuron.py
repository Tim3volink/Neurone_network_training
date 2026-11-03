import math

class Neuron:
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias
        self.z = 0
        self.y = 0

    def ponderer_sum(self, entries):
        self.z = self.bias
        for i in range(0, len(self.weight)):
            self.z += entries[i] * self.weight[i]
        return self.z

    def sigmoid(self):
        self.y = 1 / (1 + (math.e ** (-1 * self.z)))
        return self.y