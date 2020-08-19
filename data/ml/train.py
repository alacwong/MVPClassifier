# moduel to  perceptron
import numpy as np
from ml.perceptron import Perceptron
from typing import List


error_plot = []


def train(data: np.ndarray, labels: List, epochs=3, max_error=0.05):
    """
    Train perceptron
    :param data: training data
    :param labels: labels for data
    :param epochs: number of epochs
    :param max_error: convergence precisions
    :return: model trained with data
    """
    model = Perceptron(len(data[0]))
    num_epochs = 0
    error = 1
    while num_epochs < epochs or error < max_error:
        gradient_acc = np.array([0] * len(data[0]))
        error_acc = 0
        for i in range(len(data)):
            actual = model.fire(data[i])
            gradient = compute_gradient(model, labels[i])
            gradient_acc = np.add(gradient_acc, gradient)
            error_acc += compute_error(actual, labels[i])
        total_gradient = np.divide(gradient_acc, -len(data))
        # print(total_gradient)
        model.update(total_gradient)
        num_epochs += 1
        error = error_acc / len(data)
        error_plot.append(error)
    return model


def compute_gradient(model: Perceptron, output: float):
    """
    compute error gradient for training example
    :param model:
    :param output:
    :return:
    """
    error = []
    for i in range(len(model.weights)):
        dc = 2 * (model.output - output)
        sigmoid = 1 / (1 + np.exp(-model.sum))
        dz = sigmoid * (1 - sigmoid)
        dw = model.input[i]
        error.append(dc * dz * dw)
    return np.array(error)


def compute_error(output: float, actual: float):
    """
    compute total error
    :param actual:
    :param output:
    :return:
    """
    return np.square(actual - output)
