# Module training with sklearn
from scripts.generate_data import load_data
from scripts.numpy_util import split_data, binarize
from sklearn.neural_network import MLPRegressor
from utils.validation_util import validate_accuracy
from utils.plot_util import plot_validate, plot_error
from joblib import dump
from sklearn.linear_model import LogisticRegression

import time


def plot_accuracy():
    accuracy = []
    errors = []
    converged = False
    n = 1
    while not converged:
        regr = MLPRegressor(random_state=1, max_iter=n, hidden_layer_sizes=(1,), activation="logistic").fit(
            train, train_label)
        curr_accuracy = validate_accuracy(regr, test, test_label)
        curr_error = regr.score(test, test_label)
        print('Current accuracy: %f Curr error: %f' % (curr_accuracy, curr_error))
        accuracy.append(curr_accuracy)
        errors.append(curr_error)
        converged = n != regr.n_iter_
        n += 1

    plot_validate(accuracy)
    plot_error(errors)


dates = [
    '../csv/' + str(x) + '.csv' for x in range(1980, 2020)
]
data, labels, players = load_data(dates)
train, train_label, test, test_label = split_data(0.8, data, labels)

# perceptron regressor, what if we try different models?
regr = MLPRegressor(random_state=1, max_iter=500, verbose=True, hidden_layer_sizes=(1,), activation="logistic").fit(
    train, train_label)

# regr = MLPRegressor(random_state=1, max_iter=500, verbose=True, hidden_layer_sizes=(2,), activation="logistic").fit(
#     train, train_label)

print(regr.coefs_)
pred = regr.predict(test)
total = 0
correct = 0
for i in range(len(pred)):
    if binarize(pred[i]) == test_label[i]:
        correct += 1
    total += 1
print("Accuracy: %f %d / %d" % (correct / total, correct, total))
for x in regr.coefs_:
    for y in x:
        print(y[0])
    print('******')

dump(regr, '2_layer_nn.joblib')
