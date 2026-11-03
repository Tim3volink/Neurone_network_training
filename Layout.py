from Neuron import Neuron

class Layout:
    def __init__(self, neurons):
        self.neurons = neurons

    def active(self, entries):
        activations = []
        for neuron in self.neurons:
            neuron.ponderer_sum(entries)
            activations.append(neuron.sigmoid())
        return activations

n1 = Neuron([1, 0], 0)
n2 = Neuron([0, 1], 0)
n3 = Neuron([1, 1], 0)

layer = Layout([n1, n2, n3])

print(layer.neurons)
print(len(layer.neurons))

entrees = [1, 2]
result = layer.active(entrees)
print(result)

entrees = [2, 1]
result = layer.active(entrees)
print(result)

layer2 = Layout([n1])
entrees = [1, 2]
result = layer2.active(entrees)
print(result)