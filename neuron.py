import random
# ERROR IN A BASE LOGIC! NOT THE MEAN OF DENDRITES, NEED TO MAKE DENDRITES ACTIVATION CHECK!
# Fixed, now neurons should only work when activated by an activation matrix.
# Neuron could polarize and depolarize, this should be reflected somehow in the model.
# Assumption 1. Depolarization could lead to a stronger connection with other neuron,
# Which provides better output for a system.


class Neuron:
	"""Basic neuron class intended for simulating a neuron"""

	# Initialization.
	def __init__(self, initialize_dendrites):
		self.dendrites = {}
		self.activation_matrix = []
		self.power_matrix = []
		self.nucleus_threshold = 0.8
		self.nucleus = 0
		# Dendrites base activation.
		x = 0
		while x < initialize_dendrites:
			self.dendrites["dendrite_" + str(x)] = 0
			self.activation_matrix.append(0)
			x += 1
	
	# Assume, the power to activate a neuron could be positive or negative.
	# Initial state is random
	def randomize_dendrites(self):
		"""Randomly allocating power of dendrites"""
		for dendrite in self.dendrites:
			self.dendrites[dendrite] = (random.randint(1,200) - 100) / 100

	# Cogitation process, compare activation vs mean sum of dendrites.
	def cogitate(self, *activation_matrix):
		"""Cogitation process"""
		# Checking new activation parameters.
		if activation_matrix:
			self.activation_matrix = activation_matrix

		# Building power matrix out of activation matrix and dendrites power.
		for x in range(0, len(self.activation_matrix)):
			if self.activation_matrix[x] == 1:
				dendrite_power = self.dendrites["dendrite_" + str(x)]
				self.power_matrix.append(dendrite_power)

		# Generating average from power matrix.
		power_matrix = self.power_matrix
		try:
			power_matrix_average = sum(power_matrix) / len(power_matrix)
		except ZeroDivisionError:
		# If there are no active dendrites, avoid 0 division, by giving 0.
			power_matrix_average = 0
		nucleus_threshold = self.nucleus_threshold

		# Checking activation.
		if power_matrix_average >= nucleus_threshold:
			self.nucleus = 1
		else:
			self.nucleus = 0