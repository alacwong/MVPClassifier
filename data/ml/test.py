# testing model effectiveness on all players
from scripts.generate_data import load_raw, load_data
from joblib import load
import pickle

from scripts.numpy_util import split_data, binarize

model = load('scikit-perceptron.joblib')

dates = [
    '../csv/' + str(x) + '.csv' for x in range(2018, 2019)
]
data, labels, all_players = load_data(dates)
print(len(all_players), len(data))
train, train_label, test, test_label = split_data(0, data, labels)

print(dates)

pred = model.predict(test)

print(len(pred), len(all_players))
for i in range(len(pred)):
    p1, p2 = all_players[i]
    if binarize(pred[i]):
        print(f'{p1} > {p2} by {pred[i]}')
    else:
        print(f'{p2} > {p1} by { 1 - pred[i]}')

# total = 0
# correct = 0
# for i in range(len(pred)):
#     if binarize(pred[i]) == test_label[i]:
#         correct += 1
#     total += 1
# print("Accuracy: %f %d / %d" % (correct / total, correct, total))


