import json

# Neural network main code.
from neuron import Neuron

first_neuron = Neuron(4)


datasets = {"data_1": {"matrix": [1, 1, 1, 1], "expected": 1},
"data_2": {"matrix": [1, 0, 1, 1], "expected": 1},
"data_3": {"matrix": [0, 1, 0, 1], "expected": 1},
"data_4": {"matrix": [0, 0, 0, 1], "expected": 1},
"data_5": {"matrix": [0, 0, 1, 0], "expected": 0},
"data_6": {"matrix": [1, 0, 1, 0], "expected": 0},
"data_7": {"matrix": [1, 0, 0, 0], "expected": 0},
"data_8": {"matrix": [1, 1, 1, 0], "expected": 0},
}

learned_datasets = first_neuron.learn_datasets(datasets)


filename = "value_matrix.json"

with open(filename, 'w') as f_obj:
	f_obj.write(json.dumps(learned_datasets, indent=4, sort_keys=False))

