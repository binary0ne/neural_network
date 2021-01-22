import unittest
import random
from neuron import Neuron

class TestNeuron(unittest.TestCase):
	"""Neuron test class"""
	def test_dendrites_initialization(self):
		"""Testing initialize_dendrites method"""
		my_neuron = Neuron()
		my_neuron.initialize_dendrites(5)
		test_dendrite = "dendrite_4"

		self.assertIn(test_dendrite, my_neuron.dendrites)

	def test_activation_matrix_default_sum(self):
		"""Is activation matrix sum default is 0's
		(range from 0 to 100?"""
		for x in range(0, 101):
			my_neuron = Neuron(x)
			sum_of_matrix = sum(my_neuron.activation_matrix)

			self.assertEqual(0, sum_of_matrix)

	def test_activation_matrix_default_len(self):
		"""Is activation matrix quantity is the same as declared
		(range from 0 to 100)?"""
		for x in range(0,101):
			my_neuron = Neuron(x)
			len_of_matrix = len(my_neuron.activation_matrix)

			self.assertEqual(x, len_of_matrix)

	def test_activation_zero_power(self):
		"""Is neuron activated with zero dendrites power?"""
		dendrites_config = {"dendrite_0": 0, "dendrite_1": 0,
			"dendrite_2": 0, "dendrite_3": 0,
			}
		my_neuron = Neuron(4)
		my_neuron.dendrites = dendrites_config
		my_neuron.cogitate()

		self.assertEqual(0, my_neuron.nucleus)

	def test_activation_maximum_power(self):
		"""Is neuron activated with maximum dendrites power?"""
		dendrites_config = {"dendrite_0": 100, "dendrite_1": 100,
			"dendrite_2": 100, "dendrite_3": 100,
			}
		my_neuron = Neuron(4)
		my_neuron.dendrites = dendrites_config
		my_neuron.activation_matrix = [1, 1, 1, 1]
		my_neuron.cogitate()

		self.assertEqual(1, my_neuron.nucleus)

	def test_activation_by_matrix_and_power(self):
		"""Check does matrix with power activate nucleus correctly?"""
		dendrites_config = {"dendrite_0": 1, "dendrite_1": 1,
			"dendrite_2": 0, "dendrite_3": 1,
			}
		my_neuron = Neuron(4)
		my_neuron.dendrites = dendrites_config
		my_neuron.activation_matrix = [0, 0, 1, 0]
		my_neuron.cogitate()

		self.assertEqual(0, my_neuron.nucleus)

	def test_overrwrite_dendrites_parameters_by_arguments(self):
		"""Will activation matrix change and work correctly with 
		overwrited arguments from cogitate() method?"""
		dendrites_config = {"dendrite_0": 0, "dendrite_1": 1,
			"dendrite_2": 0, "dendrite_3": 0,
			}
		my_neuron = Neuron(4)
		my_neuron.dendrites = dendrites_config
		my_neuron.activation_matrix = [1, 0, 0, 0]
		new_activation_matrix = [0, 1, 0, 0]
		my_neuron.cogitate(new_activation_matrix)


		self.assertEqual(new_activation_matrix, my_neuron.activation_matrix)

	def test_power_matrix_generation(self):
		"""Will power matrix be generated correctly with random dendrites
		and activation matrix provided?"""
		# Testing it 1000 times.
		for iteration in range(0, 1001):
			# Random dendrites numbers, from 1 to 200.
			dendrites_amount = random.randint(1,200)
			my_neuron = Neuron(dendrites_amount)
			activation_matrix = []

			# Generating random activation matrix.
			for x in range(0, dendrites_amount):
				activation_matrix.append(random.randint(0,1))

			# Randomizing dendrites power.
			my_neuron.randomize_dendrites()

			# Writing new power matrix through parametrized cogitation.
			my_neuron.cogitate(activation_matrix)

			# Grabbing testing dendrites power list.
			dendrites_power = []
			for x in my_neuron.dendrites.values():
				dendrites_power.append(x)

			# Generate testing power matrix
			power_matrix = []
			n = 0
			for x in activation_matrix:
				if x == 1:
					power_matrix.append(int(dendrites_power[n]))
				n += 1

			self.assertEqual(power_matrix, my_neuron.power_matrix)

	def test_random_cogitation_result(self):
		"""Will cogitation be correct with random parameters?"""
		# Testing it 1000 times.
		for iteration in range(0, 1001):
			# Random dendrites numbers, from 1 to 200.
			dendrites_amount = random.randint(1,200)
			my_neuron = Neuron(dendrites_amount)
			activation_matrix = []

			# Generating random activation matrix.
			for x in range(0, dendrites_amount):
				activation_matrix.append(random.randint(0,1))

			# Randomizing dendrites power.
			my_neuron.randomize_dendrites()

			# Generating random nucleus threshold.
			nucleus_threshold = random.randint(0, 100)
			my_neuron.nucleus_threshold = nucleus_threshold

			# Writing new power matrix through parametrized cogitation.
			my_neuron.cogitate(activation_matrix)

			# Grabbing testing dendrites power list.
			dendrites_power = []
			for x in my_neuron.dendrites.values():
				dendrites_power.append(x)

			# Generate testing power matrix
			power_matrix = []
			n = 0
			for x in activation_matrix:
				if x == 1:
					power_matrix.append(int(dendrites_power[n]))
				n += 1

			# Generating average from power matrix.
			try:
				power_matrix_average = sum(power_matrix) / len(power_matrix)
			except ZeroDivisionError:
			# If there are no active dendrites, avoid 0 division, by giving 0.
				power_matrix_average = 0

			# Checking activation.
			nulceus = 0
			if power_matrix_average >= nucleus_threshold:
				nucleus = 1
			else:
				nucleus = 0

			self.assertEqual(nucleus, my_neuron.nucleus)

	def test_maximize_dendrites(self):
		"""Check, are all dendrites maximized?"""
		my_neuron = Neuron(10)
		my_neuron.maximize_dendrites()

		for value in my_neuron.dendrites.values():
			self.assertEqual(100, value)

	def test_minimize_dendrites(self):
		"""Check, are all dendrites minimized?"""
		my_neuron = Neuron(10)
		my_neuron.minimize_dendrites()

		for value in my_neuron.dendrites.values():
			self.assertEqual(-100, value)

	def test_normalize_dendrites(self):
		"""Check, are all dendrites normalized?"""
		my_neuron = Neuron(10)
		my_neuron.normalize_dendrites()

		for value in my_neuron.dendrites.values():
			self.assertEqual(0, value)

	def test_normalize_dendrites_withlist(self):
		"""Check, are all dendrites normalized?"""
		my_neuron = Neuron(10)
		my_neuron.dendrites["dendrite_5"] = 50
		my_neuron.normalize_dendrites(["dendrite_5"])

		for dendrite in my_neuron.dendrites:
			if dendrite == "dendrite_5":
				self.assertEqual(50, my_neuron.dendrites[dendrite])
			else:
				self.assertEqual(0, my_neuron.dendrites[dendrite])

	def test_learning_capabilities_positive_result(self):
		"""Will test ability of neuron to adapt to a static data input with
		positive expected result"""
		dataset = [1, 0, 1, 0]
		expected_result = 1
		my_neuron = Neuron(len(dataset))
		my_neuron.learn(expected_result, dataset)

		self.assertEqual(expected_result, my_neuron.nucleus)

	def test_learning_capabilities_negative_result(self):
		"""Will test ability of neuron to adapt to a static data input with
		negative expected result"""
		dataset = [0, 1, 1, 0]
		expected_result = 0
		my_neuron = Neuron(len(dataset))
		my_neuron.nucleus = 1
		my_neuron.learn(expected_result, dataset)

		self.assertEqual(expected_result, my_neuron.nucleus)

	def test_learning_capabilities_random(self):
		"""Will test ability to learn single activation matrix"""
		for iteration in range(0, 1001):
			# Random dendrites numbers, from 1 to 20.
			dendrites_amount = random.randint(1,20)
			my_neuron = Neuron(dendrites_amount)
			activation_matrix = []

			# Generating random activation matrix and its expected result.
			for x in range(0, dendrites_amount):
				activation_matrix.append(random.randint(0,1))

			# Generating random expected result.
			expected_result = random.randint(0,1)

			my_neuron.learn(expected_result, activation_matrix)

			self.assertEqual(expected_result, my_neuron.nucleus)		

	def test_understanding_capabilities(self):
		"""Will test ability to find pattern from datasets"""
		dataset_len = 8
		first_neuron = Neuron(dataset_len)

		datasets ={}
		for x in range(0,500):
			datasets["data_" + str(x)] ={}

		for dataset in datasets:
			matrix = []
			for x in range(0, dataset_len):
				z = random.randint(0, 1)
				matrix.append(z)
			datasets[dataset]["matrix"] = matrix
			if matrix[0] == 1 and matrix[1] == 0:
				datasets[dataset]["expected"] = 1
			else:
				datasets[dataset]["expected"] = 0


		first_neuron.understand_learned(datasets)

		self.assertEqual(1, first_neuron.predict([1, 0, 0, 1, 0, 0, 0, 1]))
		self.assertEqual(0, first_neuron.predict([1, 1, 0, 1, 1, 1, 1, 1]))
		self.assertEqual(1, first_neuron.predict([1, 0, 1, 1, 1, 1, 1, 1]))


unittest.main()