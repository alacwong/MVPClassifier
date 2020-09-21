# main file, run analytics on neural network]
from scripts.generate_data import load_data
from scripts.numpy_util import split_data, binarize
from ml.train import Trainer
import time
from utils.plot_util import plot_error, plot_validate




files = [
    'csv/' + str(x) + '.csv' for x in range(1980, 2020)
]
data = load_data(files)

data, labels = data
train, train_label, test, test_label = split_data(0.8, data, labels)

start = time.time()
model = Trainer(train, train_label, test, test_label)

model.train_model(max_error=0.00001, epochs=300)
plot_error(model.error_plot)
plot_validate(model.validate_plot)

end = time.time()


