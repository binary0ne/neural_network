import unittest
import random
from neuron import Neuron

class TestNeuron(unittest.TestCase):
	"""Neuron test class"""
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
		dendrites_config = {"dendrite_0": 1, "dendrite_1": 1,
			"dendrite_2": 1, "dendrite_3": 1,
			}
		my_neuron = Neuron(4)
		my_neuron.dendrites = dendrites_config
		my_neuron.activation_matrix = [1, 1, 1, 1]
		my_neuron.cogitate()

		self.assertEqual(1, my_neuron.nucleus)

	def test_activation_by_matrix_and_power(self):
		"""Check does matrix with power activate nucleus correctly?"""
		dendrites_config = {"dendrite_0": 1, "dendrite_1": 0,
			"dendrite_2": 0, "dendrite_3": 0,
			}
		my_neuron = Neuron(4)
		my_neuron.dendrites = dendrites_config
		my_neuron.activation_matrix = [1, 0, 0, 0]
		my_neuron.cogitate()

		self.assertEqual(1, my_neuron.nucleus)

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
					power_matrix.append(dendrites_power[n])
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
			nucleus_threshold = random.randint(0, 100) / 100
			my_neuron.nucleus_threshold = nucleus_threshold

			# Writing new power matrix through parametrized cogitation.
			average_from_class = my_neuron.cogitate(activation_matrix)

			# Grabbing testing dendrites power list.
			dendrites_power = []
			for x in my_neuron.dendrites.values():
				dendrites_power.append(x)

			# Generate testing power matrix
			power_matrix = []
			n = 0
			for x in activation_matrix:
				if x == 1:
					power_matrix.append(dendrites_power[n])
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
			filename = 'debug.log'

			self.assertEqual(nucleus, my_neuron.nucleus)

unittest.main()