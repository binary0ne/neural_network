import random

# Neuron could polarize and depolarize, this should be reflected somehow in the model.
# Assumption 1. Depolarization could lead to a stronger connection with other neuron,
# Which provides better output for a system.


class Neuron:
	"""Basic neuron class intended for simulating a neuron"""

	# Initialization.
	def __init__(self, initialize_dendrites):
		self.initialize_dendrites = initialize_dendrites
		self.dendrites = {}
		self.activation_threshold = 0.8
	
	# Dendrites base activation.
	def init_dendrites(self):
		"""Creating dendrites out of proposed amount number"""
		x = 0
		while x < self.initialize_dendrites:
			x += 1
			self.dendrites["dendrite_" + str(x)] = 0

	# Assume, the power to activate a neuron could be positive or negative.
	# Initial state is random
	def randomize_dendrites(self):
		"""Randomly allocating power of dendrites"""
		for dendrite in self.dendrites:
			self.dendrites[dendrite] = (random.randint(1,200) - 100) / 100

	# Cogitation process, compare activation vs mean sum of dendrites.
	def cogitate(self, *input_data):
		"""Cogitation process"""
		# Defining variables.
		dendrites_sum = sum(self.dendrites.values())
		dendrites_mean = dendrites_sum / self.initialize_dendrites
		activation_threshold = self.activation_threshold

		# Checking activation.
		if dendrites_mean >= activation_threshold:
			return 1
		else:
			return 0





first_neuron = Neuron(4)
first_neuron.init_dendrites()
first_neuron.randomize_dendrites()
epochs = 0
while first_neuron.cogitate() != 1:
	first_neuron.randomize_dendrites()
	epochs += 1
for name, power in first_neuron.dendrites.items():
	print(name + " " + str(power))
print(epochs)


