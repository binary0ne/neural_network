import json
import random
# Neural network main code.
from neuron import Neuron

dataset_len = 8
first_neuron = Neuron(dataset_len)

datasets ={}
for x in range(0,2000):
	datasets["data_" + str(x)] ={}

for dataset in datasets:
	matrix = []
	for x in range(0, dataset_len):
		z = random.randint(0, 1)
		matrix.append(z)
	datasets[dataset]["matrix"] = matrix
	if matrix[0] == 1 and matrix[1] == 1 and matrix[2] == 0:
		datasets[dataset]["expected"] = 1
	else:
		datasets[dataset]["expected"] = 0

old_expected = 0
dataset_to_delete = []
for dataset in datasets:
	if datasets[dataset]["expected"] == old_expected:
		old_expected = datasets[dataset]["expected"]
		dataset_to_delete.append(dataset)
	else:
		old_expected = datasets[dataset]["expected"]

for dataset in dataset_to_delete:
	del datasets[dataset]


learned_datasets = first_neuron.learn_datasets(datasets)


filename = "value_matrix.json"

with open(filename, 'w') as f_obj:
	f_obj.write(json.dumps(learned_datasets, indent=4, sort_keys=False))

first_neuron.understand_learned(datasets)
print(first_neuron.predict([1, 0, 0, 1, 1, 1, 1, 1]))
print(first_neuron.predict([1, 1, 1, 1, 1, 1, 1, 1]))
print(first_neuron.predict([1, 1, 0, 1, 1, 1, 1, 1]))
print(first_neuron.predict([1, 0, 0, 0, 0, 0, 0, 0]))
print(first_neuron.predict([1, 1, 1, 0, 0, 0, 0, 0]))
print(first_neuron.predict([1, 1, 0, 0, 0, 0, 0, 0]))