import json

# Neural network main code.
from neuron import Neuron

first_neuron = Neuron(3)

data_set_1 = [1, 1, 0]
expected_result = 1
nucleus_threshold = 50
first_neuron.find_activation_window(expected_result, nucleus_threshold, data_set_1)


filename = "value_matrix.json"

with open(filename, 'w') as f_obj:
	f_obj.write(json.dumps(first_neuron.value_matrix, indent=4, sort_keys=True))