# moduel to  perceptron
import numpy as np
from ml.perceptron import Perceptron
from typing import List
from scripts.numpy_util import binarize

error_plot = []
validate_plot = []
num_epochs = 0


def train(train: List, train_labels: List, test, test_labels, epochs=300, max_error=0.05):
    """
    Train perceptron
    :param test_labels: test data
    :param test: labels for testing
    :param train: training data
    :param train_labels: labels for data
    :param epochs: number of epochs
    :param max_error: convergence precisions
    :return: model trained with data
    """
    model = Perceptron(len(train[0]))
    error = 1
    prev_error = 2
    global num_epochs
    while num_epochs < epochs and prev_error - error > 0.000001:
        validate(model, test, test_labels)
        gradient_acc = np.array([0] * len(train[0]))
        error_acc = 0
        for i in range(len(train)):
            actual = model.fire(train[i])
            gradient = compute_gradient(model, train_labels[i])
            gradient_acc = np.add(gradient_acc, gradient)
            error_acc += compute_error(actual, train_labels[i])
        total_gradient = np.divide(gradient_acc, -len(train))
        model.update(total_gradient)
        num_epochs += 1
        prev_error = error
        error = error_acc / len(train)
        error_plot.append(error)
        print(prev_error, error)
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


def validate(model, test, test_labels):
    """
    validate
    :param model:
    :param test:
    :param test_labels:
    :return:
    """
    correct = 0
    for i in range(len(test)):
        output = binarize(model.fire(test[i]))
        if output == test_labels[i]:
            correct += 1
    validate_plot.append(correct / len(test))
