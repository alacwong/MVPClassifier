# main file, run analytics on neural network]
from scripts.generate_data import get_data
import ml.train as ml
import time
import matplotlib.pyplot as plt

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
data = get_data(urls)

train, labels = data
start = time.time()
model = ml.train(train, labels, epochs=300)
end = time.time()
print('Trained 500 iterations in %f s' %(end-start))
print('Final error %f' %(ml.error_plot[-1]))
plt.plot([i for i in range(len(ml.error_plot))], ml.error_plot)
plt.ylabel('Error')
plt.xlabel('Epochs')
plt.show()

print(model.weights)