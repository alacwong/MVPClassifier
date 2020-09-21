# moduel to  perceptron
import numpy as np
from ml.perceptron import Perceptron
from typing import List
from scripts.numpy_util import binarize
from random import randint


def compute_error(output: float, actual: float):
    """
    compute total error
    :param actual:
    :param output:
    :return:
    """
    return np.square(actual - output)


class Trainer:

    def train_model(self, epochs=300, max_error=0.05):
        """
        Train perceptron
        :param epochs: number of epochs
        :param max_error: convergence precisions
        :return: model trained with data
        """
        error, prev_error = [1, 2]
        while self.num_epochs < epochs and prev_error - error > max_error:
            self.validate()
            prev_error = error
            gradient, error = self.get_mean_gradient()
            self.model.update(gradient)
            self.error_plot.append(error)
            self.num_epochs += 1
            print(prev_error, error)

    def get_mean_gradient(self):
        """
        compute average gradient
        :training training data
        :return:
        """
        gradient_acc = np.array([0] * len(self.train[0]))
        error_acc = 0
        for i in range(len(self.train)):
            actual = self.model.fire(self.train[i])
            gradient = self.compute_gradient(self.train_labels[i])
            gradient_acc = np.add(gradient_acc, gradient)
            error_acc += compute_error(actual, self.train_labels[i])
        return [np.divide(gradient_acc, -len(self.train)), error_acc / len(self.train)]

    def get_batch_gradient(self, n):
        """
        Generate batch gradient vector from batch size n
        :param n: size of batch
        :return:
        """

    def get_stochastic_gradient(self):
        """
        Generate stochastic gradient
        :return:
        """
        index = randint(0, len(self.train))
        actual = self.model.fire(self.train[index])
        gradient = self.compute_gradient(self.train_labels[index])
        return gradient, compute_error(actual, self.train_labels[index])

    def compute_gradient(self, output: float):
        """
        compute error gradient for training example
        :param output:
        :return:
        """
        error = []
        for i in range(len(self.model.weights)):
            dc = 2 * (self.model.output - output)
            sigmoid = 1 / (1 + np.exp(-self.model.sum))
            dz = sigmoid * (1 - sigmoid)
            dw = self.model.input[i]
            error.append(dc * dz * dw)
        return np.array(error)

    def validate(self):
        """
        validate
        :return:
        """
        correct = 0
        for i in range(len(self.test)):
            output = binarize(self.model.fire(self.test[i]))
            if output == self.test_labels[i]:
                correct += 1
        self.validate_plot.append(correct / len(self.test))

    def __init__(self, train: List, train_labels: List, test, test_labels):
        self.error_plot = []
        self.validate_plot = []
        self.num_epochs = 0
        self.train = train
        self.train_labels = train_labels
        self.test = test
        self.test_labels = test_labels
        self.model = Perceptron(len(self.train[0]))
