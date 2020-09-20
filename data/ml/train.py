# moduel to  perceptron
import numpy as np
from ml.perceptron import Perceptron
from typing import List
from scripts.numpy_util import binarize


def compute_error(output: float, actual: float):
    """
    compute total error
    :param actual:
    :param output:
    :return:
    """
    return np.square(actual - output)


class Trainer():
    error_plot = []
    validate_plot = []
    num_epochs = 0

    def train(self, epochs=300, max_error=0.05):
        """
        Train perceptron
        :param epochs: number of epochs
        :param max_error: convergence precisions
        :return: model trained with data
        """
        model = Perceptron(len(self.train[0]))
        error = 1
        prev_error = 2
        while self.num_epochs < epochs and prev_error - error > 0.0001:
            self.validate(model, self.test, self.test_labels)
            gradient_acc = np.array([0] * len(self.train[0]))
            error_acc = 0
            for i in range(len(self.train)):
                actual = model.fire(self.train[i])
                gradient = self.compute_gradient(model, self.train_labels[i])
                gradient_acc = np.add(gradient_acc, gradient)
                error_acc += compute_error(actual, self.train_labels[i])
            total_gradient = np.divide(gradient_acc, -len(self.train))
            model.update(total_gradient)
            self.num_epochs += 1
            prev_error = error
            error = error_acc / len(self.train)
            self.error_plot.append(error)
            print(prev_error, error)
        return model

    def get_total_gradient(self):
        """
        compute average gradient
        :training training data
        :return:
        """
        # for i in range(len(train)):
        #     actual = model.fire(train[i])
        #     gradient = compute_gradient(model, train_labels[i])
        #     gradient_acc = np.add(gradient_acc, gradient)
        #     error_acc += compute_error(actual, train_labels[i])
        # total_gradient = np.divide(gradient_acc, -len(train))

    def get_batch_gradient(self, n):
        """
        Generatye batch graident vector from batch size n
        :param training: trainig data
        :param n: size of batch
        :return:
        """

    def get_stochastic_gradient(self):
        """
        Generate stochastic gradient
        :param training: training data
        :return:
        """

    def compute_gradient(self, output: float):
        """
        compute error gradient for training example
        :param model:
        :param output:
        :return:
        """
        error = []
        for i in range(len(self.model.weights)):
            dc = 2 * (self.model.output - output)
            sigmoid = 1 / (1 + np.exp(-self.sum))
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
