import random

inputs = [5]
weight = 1
bias = 0

class Neuron:
    def __init__(self) -> None:
        self.bias = 0
        self.weight = random.random()
        self.output = 0
    
    def forward(self, inputs):
        self.output = inputs * self.weight + self.bias
        return self.output

neuron = Neuron()

for i in range(10):
    neuron.forward(i)
    print(i, neuron.output)

