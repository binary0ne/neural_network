import random
# ERROR IN A BASE LOGIC! NOT THE MEAN OF DENDRITES, NEED TO MAKE DENDRITES ACTIVATION CHECK!
# Neuron could polarize and depolarize, this should be reflected somehow in the model.
# Assumption 1. Depolarization could lead to a stronger connection with other neuron,
# Which provides better output for a system.


class Neuron:
	"""Basic neuron class intended for simulating a neuron"""

	# Initialization.
	def __init__(self, initialize_dendrites):
		self.initialize_dendrites = initialize_dendrites
		self.dendrites = {}
		self.activation_matrix = []
		self.nucleus_threshold = 0.8
		self.nucleus = 0
		# Dendrites base activation.
		x = 0
		while x < self.initialize_dendrites:
			x += 1
			self.dendrites["dendrite_" + str(x)] = 0
			self.activation_matrix.append(0)
	
	# Assume, the power to activate a neuron could be positive or negative.
	# Initial state is random
	def randomize_dendrites(self):
		"""Randomly allocating power of dendrites"""
		for dendrite in self.dendrites:
			self.dendrites[dendrite] = (random.randint(1,200) - 100) / 100

	# Cogitation process, compare activation vs mean sum of dendrites.
	def cogitate(self, *activation_matrix):
		"""Cogitation process"""
		# Defining variables.
		dendrites_sum = sum(self.dendrites.values())
		dendrites_mean = dendrites_sum / self.initialize_dendrites
		nucleus_threshold = self.nucleus_threshold

		# Checking activation.
		if dendrites_mean >= nucleus_threshold:
			self.nucleus = 1
		else:
			self.nucleus = 0