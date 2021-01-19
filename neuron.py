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
		self.nucleus_threshold = 100
		self.nucleus = 0
		self.valuable_dendrites = {}
		self.value_matrix = {}

		# Dendrites base activation.
		x = 0
		while x < initialize_dendrites:
			self.dendrites["dendrite_" + str(x)] = 0
			self.activation_matrix.append(0)
			x += 1
	
	# Assume, the power to activate a neuron could be positive or negative.
	# Different dendrites presets.
	def randomize_dendrites(self):
		"""Randomly allocating power of dendrites"""
		for dendrite in self.dendrites:
			self.dendrites[dendrite] = (random.randint(1,200) - 100)

	def maximize_dendrites(self):
		"""Maximizing dendrites power"""
		for dendrite in self.dendrites:
			self.dendrites[dendrite] = 100

	def minimize_dendrites(self):
		"""Minimizing dendrites power"""
		for dendrite in self.dendrites:
			self.dendrites[dendrite] = -100

	def normalize_dendrites(self, valuable_dendrites=""):
		"""Setting power = 0 to unvaluable dendrites if list is provided
		exclude provided dendrites from normalization"""
		if valuable_dendrites:
			self.valuable_dendrites = valuable_dendrites[:]
		for dendrite in self.dendrites:
			if dendrite in self.valuable_dendrites:
				continue
			self.dendrites[dendrite] = 0

	def setup_dendrites(self, target_settings):
		"""Set dendrites power on targeted value"""
		for dendrite in self.dendrites:
			self.dendrites[dendrite] = target_settings		

	# Cogitation process, compare activation vs mean sum of dendrites.
	def cogitate(self, activation_matrix=""):
		"""Cogitation process"""
		# Resetting power matrix.
		self.power_matrix = []
		# Checking new activation parameters.
		if activation_matrix:
			self.activation_matrix = activation_matrix

		# Building power matrix out of activation matrix and dendrites power.
		for x in range(0, len(self.activation_matrix)):
			if self.activation_matrix[x] == 1:
				dendrite_power = self.dendrites["dendrite_" + str(x)]
				self.power_matrix.append(int(dendrite_power))

		# Generating average from power matrix.
		power_matrix = self.power_matrix
		try:
			power_matrix_average = (sum(power_matrix)) / len(power_matrix)
		except ZeroDivisionError:
		# If there are no active dendrites, avoid 0 division, by giving 0.
			power_matrix_average = 0

		# Checking activation.
		if power_matrix_average >= self.nucleus_threshold:
			self.nucleus = 1
		else:
			self.nucleus = 0

	def find_activation_window(self, expected_result, nucleus_threshold, activation_matrix=""):
		"""Finding activation window with given parameters"""
		self.nucleus_threshold = nucleus_threshold
		if activation_matrix:
			self.activation_matrix = activation_matrix
		for dendrite in self.dendrites:
			active_array = []
			self.maximize_dendrites()
			self.cogitate()
			if self.nucleus == expected_result:
				while self.nucleus == expected_result and self.dendrites[dendrite] >= -100:
					active_array.append(self.dendrites[dendrite])
					self.dendrites[dendrite] -= 1
					self.cogitate()
			elif self.nucleus != expected_result:
				while self.nucleus != expected_result and self.dendrites[dendrite] >= -100:
					self.dendrites[dendrite] -= 1
					self.cogitate()
				while self.nucleus == expected_result and self.dendrites[dendrite] >= -100:
					active_array.append(self.dendrites[dendrite])
					self.dendrites[dendrite] -= 1
					self.cogitate()
					
			if not active_array:
				for x in range(0, 201):
					active_array.append(x - 100)

			print(sorted(active_array))		


	def build_value_matrix(self, activation_matrix=""):
		"""Finding responsible for result dendrites"""


	# Learning method for a neuron.
	def learn(self, expected_result, activation_matrix=""):
		"""Allows to "train" neuron by altering dendrite powers"""
