# Neural network main code.
from neuron import Neuron

first_neuron = Neuron(4)
first_neuron.init_dendrites()
first_neuron.randomize_dendrites()
epochs = 0
while first_neuron.cogitate() != 1:
	first_neuron.randomize_dendrites()
	epochs += 1
for name, power in first_neuron.dendrites.items():
	print(name + " " + str(power))
print(epochs)