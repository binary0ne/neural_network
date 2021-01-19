# Neural network main code.
from neuron import Neuron

first_neuron = Neuron(7)
first_neuron.randomize_dendrites()
data_set = [0, 0, 0, 0, 0, 1, 1]
first_neuron.learn(1, data_set)
print(first_neuron.nucleus)
print(first_neuron.dendrites)

first_neuron.cogitate([0, 0, 0, 0, 0, 1, 1])
print(first_neuron.nucleus)

first_neuron.cogitate([0, 0, 0, 0, 1, 1, 1])
print(first_neuron.nucleus)

first_neuron.cogitate([1, 1, 1, 1, 1, 1, 1])
print(first_neuron.nucleus)