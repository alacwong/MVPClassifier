# main file, run analytics on neural network]
from scripts.generate_data import get_data
from scripts.numpy_util import split_data, binarize
import ml.train as ml
import time
import matplotlib.pyplot as plt


def plot_error():
    plt.plot([i for i in range(len(ml.error_plot))], ml.error_plot)
    plt.ylabel('Error')
    plt.xlabel('Epochs')
    plt.show()


def plot_validate():
    plt.plot([i for i in range(len(ml.validate_plot))], ml.validate_plot)
    plt.ylabel('Accuracy')
    plt.xlabel('Epochs')
    plt.show()


# ( mvps-votings, team-wins)
urls = [
    (
        'https://www.basketball-reference.com/awards/awards_' + str(x) + '.html',
        'https://www.basketball-reference.com/leagues/NBA_' + str(x) + '_standings.html'
    )
    for x in range(1980, 2020)  # include era of 3 point
]

# subset of total urls

test = urls[-1:-5:-1]
data = get_data(test)

data, labels = data
train, train_label, test, test_label = split_data(0.8, data, labels)

start = time.time()
model = ml.train(train, labels, test, test_label, epochs=200)
end = time.time()
print('Trained 50 iterations in %f s' % (end - start))
print('Final error %f' % (ml.error_plot[-1]))
plot_error()
plot_validate()

accuracy = 0
for i in range(len(test)):
    output = model.fire(test[i])
    print('Example ' + str(i), test[i])
    print('Conifidence: %f' %(output))
    print('Output %d' % (binarize(output)))
    print('Expected %d' % (test_label[i]))
    accuracy += binarize(output)
    print('Current Accuracy %f' % (accuracy/(i + 1)))


# print(model.weights)
