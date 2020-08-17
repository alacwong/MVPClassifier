import numpy as np


class Perceptron:

    def __init__(self, data: np.ndarray, labels: np.ndarray):
        self.data = data
        self.labels = labels
        num_features = len(data[0])

    def cost(self, output: np.ndarray, index: np.ndarray):
        """
        cost function
        :return: cost
        """
        error = np.square(np.subtract(output, index))
        return np.sum(error)

    def train(self):
        """
        train model
        """

    def activation(self, x: float) -> float:
        """
        activation function
        :param x: value
        :return:
        """
        value = 1/(1 + np.exp(-x))
        return np.array([value, 1-value])
