# main file, run analytics on neural network]
from scripts.generate_data import load_data
from scripts.numpy_util import split_data, binarize
import ml.train as ml
import time
import matplotlib.pyplot as plt





files = [
    'csv/' + str(x) + '.csv' for x in range(1980, 2020)
]
data = load_data(files)

data, labels = data
train, train_label, test, test_label = split_data(0.8, data, labels)

start = time.time()
model = ml.train(train, labels, test, test_label, epochs=300)
end = time.time()
print('Trained on %d iterations' % ml.num_epochs)
print('Final error %f' % (ml.error_plot[-1]))
plot_error()
plot_validate()

accuracy = 0
for i in range(len(test)):
    output = model.fire(test[i])
    if test_label[i] == binarize(output):
        accuracy += 1
print('Total Accuracy: %f' % (accuracy / len(test)))
print(model.weights)
