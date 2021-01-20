import json

# Neural network main code.
from neuron import Neuron

data_set_1 = [0, 0, 0]
first_neuron = Neuron(len(data_set_1))
expected_result = 1
first_neuron.learn(expected_result, data_set_1)

filename = "value_matrix.json"

with open(filename, 'w') as f_obj:
	f_obj.write(json.dumps(first_neuron.value_matrix, indent=4, sort_keys=True))

first_neuron.cogitate(data_set_1)
print(first_neuron.nucleus)
print(first_neuron.nucleus_threshold)