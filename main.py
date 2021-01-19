import json

# Neural network main code.
from neuron import Neuron

first_neuron = Neuron(3)

data_set_1 = [1, 1, 1]
first_neuron.build_value_matrix(data_set_1)
print(first_neuron.valuable_dendrites)
print(first_neuron.dendrites)
print(first_neuron.value_matrix)

filename = "value_matrix.json"

with open(filename, 'w') as f_obj:
	f_obj.write(json.dumps(first_neuron.value_matrix, indent=4, sort_keys=True))