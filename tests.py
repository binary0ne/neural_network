import unittest
from neuron import Neuron

class TestNeuron(unittest.TestCase):
	"""Neuron test class"""
	def test_activation_matrix_default_sum(self):
		"""Is activation matrix sum default is 0's
		(range from 1 to 100?"""
		for x in range(0, 101):
			my_neuron = Neuron(x)
			sum_of_matrix = sum(my_neuron.activation_matrix)

			self.assertEqual(0, sum_of_matrix)

	def test_activation_matrix_default_len(self):
		"""Is activation matrix quantity is the same as declared
		(range from 1 to 100)?"""
		for x in range(0,101):
			my_neuron = Neuron(x)
			len_of_matrix = len(my_neuron.activation_matrix)

			self.assertEqual(x, len_of_matrix)

	def test_activation_zero_power(self):
		"""Is neuron activated with zero dendrites power?"""
		dendrites_config = {"dendrite_1": 0, "dendrite_2": 0,
			"dendrite_3": 0, "dendrite_4": 0,
			}
		my_neuron = Neuron(4)
		my_neuron.dendrites = dendrites_config
		my_neuron.cogitate()

		self.assertEqual(0, my_neuron.nucleus)

	def test_activation_maximum_power(self):
		"""Is neuron activated with maximum dendrites power?"""
		dendrites_config = {"dendrite_1": 1, "dendrite_2": 1,
			"dendrite_3": 1, "dendrite_4": 1,
			}
		my_neuron = Neuron(4)
		my_neuron.dendrites = dendrites_config
		my_neuron.cogitate()

		self.assertEqual(1, my_neuron.nucleus)

unittest.main()