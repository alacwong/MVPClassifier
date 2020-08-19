import numpy as np


class Perceptron:

    def __init__(self, n):

        self.weights = np.array([np.random.uniform(-1, 1) for i in range(n)])
        self.output = 0  # activation neuron
        self.sum = 0  # weighted sum + bias
        self.input = np.ndarray([])

    def fire(self, vector: np.ndarray):
        self.input = vector
        self.sum = np.dot(vector, self.weights)
        self.activation()
        return self.output

    def activation(self):
        self.output = 1 / (1 + np.exp(-self.sum))

    def update(self, gradient: np.ndarray):
        self.weights = np.add(self.weights, gradient)
